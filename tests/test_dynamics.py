from core.scenarios import get_scenario
from core.dynamics import update_state


def print_state(step, state):
    print(f"\nStep {step}")

    print(f"Stress      : {state.stress:.3f}")
    print(f"Attention   : {state.attention:.3f}")
    print(f"Fatigue     : {state.fatigue:.3f}")
    print(f"Novelty     : {state.novelty:.3f}")
    print(f"Effort      : {state.effort:.3f}")
    print(f"Emotion     : {state.emotion:.3f}")


def test_scenario(name):

    print("\n")
    print("=" * 70)
    print(f"Testing Scenario: {name.upper()}")
    print("=" * 70)

    state, profile = get_scenario(name)

    print_state(0, state)

    for step in range(1, 11):
        update_state(state, profile)

        print_state(step, state)

def test_behavior():

    flow_state, flow_profile = get_scenario("flow")
    panic_state, panic_profile = get_scenario("panic")

    for _ in range(100):
        update_state(flow_state, flow_profile)
        update_state(panic_state, panic_profile)

    assert panic_state.stress > flow_state.stress
    assert panic_state.attention < flow_state.attention
    assert panic_state.fatigue > flow_state.fatigue

    print("\nBehavioral assertions passed!\n")

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
        print("\nRunning behavioral checks...")
        test_behavior()

if __name__ == "__main__":
    main()
