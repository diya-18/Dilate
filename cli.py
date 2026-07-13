import argparse
import matplotlib.pyplot as plt
from simulator import Simulation
from core.scenarios import get_scenario

from visualization.plotter import (
    plot_time_perception,
    plot_cognitive_state,
    plot_distortion,
    plot_phase_space,
    plot_summary,
)

from visualization.animation import animate


def print_report(simulation, scenario):

    history = simulation.history

    perceived = history["perceived_time"][-1]
    avg_distortion = sum(history["distortion"]) / len(history["distortion"])

    print("\n" + "=" * 46)
    print("                Dilate Report")
    print("=" * 46)

    print(f"\nScenario              : {scenario.capitalize()}")
    print(f"Simulation Length     : {simulation.duration} s")
    print(f"Perceived Time        : {perceived:.2f} s")

    print(f"\nAverage Distortion    : {avg_distortion:.2f}x")

    print("\nPeak Cognitive State")
    print("-" * 20)

    print(f"Stress               : {max(history['stress']):.2f}")
    print(f"Fatigue              : {max(history['fatigue']):.2f}")
    print(f"Effort               : {max(history['effort']):.2f}")

    print("\nFinal Cognitive State")
    print("-" * 21)

    print(f"Attention            : {history['attention'][-1]:.2f}")
    print(f"Novelty              : {history['novelty'][-1]:.2f}")
    print(f"Emotion              : {history['emotion'][-1]:.2f}")

    print("\n" + "=" * 46)
    print("Simulation Complete.")
    print("=" * 46)


def main():

    parser = argparse.ArgumentParser(
        prog="dilate",
        description="Dilate - Computational Simulator of Subjective Time Perception"
    )

    parser.add_argument(
        "scenario",
        choices=[
            "flow",
            "gaming",
            "meditation",
            "boredom",
            "exam",
            "panic"
        ]
    )

    parser.add_argument(
        "--duration",
        type=int,
        default=300,
        help="Simulation duration in seconds."
    )

    parser.add_argument(
        "--plot",
        choices=[
            "time",
            "cognitive",
            "distortion",
            "phase",
            "all"
        ],
        help="Generate plots."
    )

    parser.add_argument(
        "--animate",
        choices=[
            "cognitive"
        ],
        help="Animate simulation."
    )

    args = parser.parse_args()

    state, profile = get_scenario(args.scenario)

    simulation = Simulation(
        initial_state=state,
        profile=profile,
        duration=args.duration
    )

    simulation.run()

    print_report(simulation, args.scenario)

    if args.plot:

        if args.plot == "time":
            plot_time_perception(simulation.history)

        elif args.plot == "cognitive":
            plot_cognitive_state(simulation.history)

        elif args.plot == "distortion":
            plot_distortion(simulation.history)

        elif args.plot == "phase":
            plot_phase_space(simulation.history)

        elif args.plot == "all":
            plot_summary(simulation.history)
        plt.show()

    if args.animate:

        if args.animate == "cognitive":
            animate(simulation.history)


if __name__ == "__main__":
    main()