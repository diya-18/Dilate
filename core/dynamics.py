import random


def _approach(current, target, rate):
    """
    Move a value gradually toward its target.
    """
    return current + (target - current) * rate


def _noise(scale):
    return random.uniform(-scale, scale)


def update_state(state, profile, dt=1):
    """
    Advances the cognitive state by one timestep.

    The brain naturally tends toward the equilibrium defined
    by the current scenario while experiencing small random
    fluctuations and interactions between variables.
    """

    rate = profile.adaptation_rate * dt

    # ---------------------------------
    # Move toward equilibrium
    # ---------------------------------

    state.stress = (
        _approach(
            state.stress,
            profile.target_stress,
            rate
        )
        + _noise(profile.noise)
    )

    state.attention = (
        _approach(
            state.attention,
            profile.target_attention,
            rate
        )
        + _noise(profile.noise)
    )

    state.fatigue = (
        _approach(
            state.fatigue,
            profile.target_fatigue,
            rate
        )
        + _noise(profile.noise)
    )

    state.novelty = (
        _approach(
            state.novelty,
            profile.target_novelty,
            rate
        )
        + _noise(profile.noise)
    )

    state.effort = (
        _approach(
            state.effort,
            profile.target_effort,
            rate
        )
        + _noise(profile.noise)
    )

    state.emotion = (
        _approach(
            state.emotion,
            profile.target_emotion,
            rate
        )
        + _noise(profile.noise)
    )

    # ---------------------------------
    # Coupling between variables
    # ---------------------------------

    # Stress reduces attention
    state.attention -= 0.01 * state.stress

    # Fatigue also reduces attention
    state.attention -= 0.005 * state.fatigue

    # Working hard slowly increases fatigue
    state.fatigue += 0.004 * state.effort

    # Positive emotion slightly reduces stress
    if state.emotion > 0:
        state.stress -= 0.004 * state.emotion

    # Negative emotion amplifies stress
    else:
        state.stress += 0.003 * abs(state.emotion)

    # High stress slightly lowers effort
    state.effort -= 0.002 * state.stress

    # Clamp values into valid ranges
    state.clamp()