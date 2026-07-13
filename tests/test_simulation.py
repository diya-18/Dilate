from simulator import Simulation
from core.scenarios import get_scenario


def run_scenario(name):

    state, profile = get_scenario(name)

    sim = Simulation(
        initial_state=state,
        profile=profile,
        duration=300,
        timestep=1
    )

    sim.run()

    history = sim.history

    average_distortion = (
        sum(history["distortion"])
        / len(history["distortion"])
    )

    perceived_time = history["perceived_time"][-1]

    return {
        "average_distortion": average_distortion,
        "perceived_time": perceived_time
    }


def main():

    scenarios = [
        "meditation",
        "flow",
        "gaming",
        "boredom",
        "exam",
        "panic",
    ]

    results = {}

    print("=" * 70)
    print("               SIMULATION VALIDATION")
    print("=" * 70)

    for scenario in scenarios:

        summary = run_scenario(scenario)

        results[scenario] = summary["average_distortion"]

        print(f"\n{scenario.upper()}")
        print(
            f"Perceived Time     : "
            f"{summary['perceived_time']:.2f}s"
        )
        print(
            f"Average Distortion : "
            f"{summary['average_distortion']:.2f}x"
        )

    print("\n" + "=" * 70)
    print("Running Behavioural Assertions...")
    print("=" * 70)

    assert results["meditation"] < results["flow"]
    assert results["flow"] < results["gaming"]
    assert results["gaming"] < results["boredom"]
    assert results["boredom"] < results["exam"]
    assert results["exam"] < results["panic"]

    print("\n✓ Simulation behaviour validated.")

    print("\nScenario Ordering")

    ordered = sorted(
        results.items(),
        key=lambda x: x[1]
    )

    for name, value in ordered:
        print(f"{name:<12}{value:.2f}x")


if __name__ == "__main__":
    main()