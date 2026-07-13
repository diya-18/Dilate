from dataclasses import dataclass


@dataclass
class ScenarioProfile:
    """
    Long-term equilibrium for a cognitive scenario.
    """

    target_stress: float
    target_attention: float
    target_fatigue: float
    target_novelty: float
    target_effort: float
    target_emotion: float

    adaptation_rate: float
    noise: float