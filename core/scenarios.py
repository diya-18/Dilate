from core.states import BrainState
from core.profile import ScenarioProfile


def get_scenario(name):
    """
    Returns:
        (BrainState, ScenarioProfile)
    """

    scenarios = {

        "flow": (
            BrainState(
                stress=0.10,
                attention=0.90,
                fatigue=0.10,
                novelty=0.50,
                effort=0.85,
                emotion=0.60
            ),

            ScenarioProfile(
                target_stress=0.15,
                target_attention=0.95,
                target_fatigue=0.30,
                target_novelty=0.25,
                target_effort=0.85,
                target_emotion=0.60,

                adaptation_rate=0.015,
                noise=0.003
            )
        ),

        "exam": (
            BrainState(
                stress=0.60,
                attention=0.80,
                fatigue=0.20,
                novelty=0.40,
                effort=0.90,
                emotion=-0.20
            ),

            ScenarioProfile(
                target_stress=0.85,
                target_attention=0.75,
                target_fatigue=0.75,
                target_novelty=0.15,
                target_effort=0.95,
                target_emotion=-0.35,

                adaptation_rate=0.020,
                noise=0.006
            )
        ),

        "panic": (
            BrainState(
                stress=0.90,
                attention=0.45,
                fatigue=0.60,
                novelty=0.80,
                effort=1.00,
                emotion=-0.90
            ),

            ScenarioProfile(
                target_stress=0.98,
                target_attention=0.35,
                target_fatigue=0.85,
                target_novelty=0.60,
                target_effort=1.00,
                target_emotion=-0.80,

                adaptation_rate=0.030,
                noise=0.010
            )
        ),

        "gaming": (
            BrainState(
                stress=0.20,
                attention=0.85,
                fatigue=0.20,
                novelty=0.80,
                effort=0.70,
                emotion=0.75
            ),

            ScenarioProfile(
                target_stress=0.18,
                target_attention=0.92,
                target_fatigue=0.40,
                target_novelty=0.45,
                target_effort=0.75,
                target_emotion=0.70,

                adaptation_rate=0.015,
                noise=0.004
            )
        ),

        "meditation": (
            BrainState(
                stress=0.05,
                attention=0.70,
                fatigue=0.10,
                novelty=0.10,
                effort=0.25,
                emotion=0.80
            ),

            ScenarioProfile(
                target_stress=0.03,
                target_attention=0.80,
                target_fatigue=0.05,
                target_novelty=0.05,
                target_effort=0.20,
                target_emotion=0.90,

                adaptation_rate=0.012,
                noise=0.001
            )
        ),

        "boredom": (
            BrainState(
                stress=0.20,
                attention=0.25,
                fatigue=0.35,
                novelty=0.05,
                effort=0.20,
                emotion=-0.10
            ),

            ScenarioProfile(
                target_stress=0.25,
                target_attention=0.15,
                target_fatigue=0.70,
                target_novelty=0.02,
                target_effort=0.10,
                target_emotion=-0.15,

                adaptation_rate=0.018,
                noise=0.003
            )
        )

    }

    try:
        return scenarios[name]
    except KeyError:
        raise ValueError(f"Unknown scenario: {name}")