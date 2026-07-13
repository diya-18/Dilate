from core.model import TimeModel
from core.scenarios import get_scenario

# INITIAL COGNITIVE STATE VALIDATION

def test_scenario(name):
    state, _ = get_scenario(name)

    model = TimeModel()

    distortion = model.distortion(state)
    perceived = model.perceived_time(10, state)

    print("=" * 60)
    print(f"Scenario : {name.upper()}")
    print("=" * 60)

    print(f"Stress       : {state.stress:.2f}")
    print(f"Attention    : {state.attention:.2f}")
    print(f"Fatigue      : {state.fatigue:.2f}")
    print(f"Novelty      : {state.novelty:.2f}")
    print(f"Effort       : {state.effort:.2f}")
    print(f"Emotion      : {state.emotion:.2f}")

    print()

    print(f"Distortion   : {distortion:.2f}x")
    print(f"10 seconds -> {perceived:.2f} seconds")
    print()


def main():

    scenarios = [
        "flow",
        "panic",
        "exam",
        "gaming",
        "meditation",
        "boredom"
    ]

    for scenario in scenarios:
        test_scenario(scenario)


if __name__ == "__main__":
    main()