from core.constants import (
    STRESS_WEIGHT,
    ATTENTION_WEIGHT,
    FATIGUE_WEIGHT,
    NOVELTY_WEIGHT,
    EFFORT_WEIGHT,
    EMOTION_WEIGHT,
    MIN_DISTORTION,
    MAX_DISTORTION,
)


class TimeModel:
    """
    Computational model of subjective time perception.

    Distortion > 1.0
        Time feels slower (expanded).

    Distortion < 1.0
        Time feels faster (compressed).
    """

    def distortion(self, state):

        # ----------------------------
        # Individual Cognitive Effects
        # ----------------------------

        # Stress has a nonlinear influence.
        stress_effect = (
            STRESS_WEIGHT
            * (state.stress ** 2)
        )

        # Fatigue stretches perceived time.
        fatigue_effect = (
            FATIGUE_WEIGHT
            * state.fatigue
        )

        # Sustained attention compresses time.
        attention_effect = (
            ATTENTION_WEIGHT
            * state.attention
        )

        # Effort only matters when attention is low.
        effort_effect = (
            EFFORT_WEIGHT
            * state.effort
            * (1 - state.attention)
        )

        # Positive emotion compresses time.
        # Negative emotion expands time.
        if state.emotion >= 0:
            emotion_effect = (
                -EMOTION_WEIGHT
                * state.emotion
            )
        else:
            emotion_effect = (
                EMOTION_WEIGHT
                * abs(state.emotion)
            )

        # Novelty matters less when focused.
        novelty_effect = (
            NOVELTY_WEIGHT
            * state.novelty
            * (1 - state.attention)
        )

        # ----------------------------
        # Flow Bonus
        # ----------------------------

        flow_bonus = (
            0.03
            * state.attention
            * max(0.0, state.emotion)
            * (1 - state.stress)
        )

        # ----------------------------
        # Final Distortion
        # ----------------------------

        distortion = (
            1
            + stress_effect
            + fatigue_effect
            + effort_effect
            + emotion_effect
            + novelty_effect
            - attention_effect
            - flow_bonus
        )

        distortion = max(
            MIN_DISTORTION,
            min(MAX_DISTORTION, distortion)
        )

        return distortion

    def perceived_time(self, real_time, state):
        return real_time * self.distortion(state)