from dataclasses import dataclass


@dataclass
class BrainState:
    """
    Represents the current cognitive state of the simulated person.

    Every variable is normalized between 0 and 1
    except emotion, which ranges from -1 to 1.
    """

    stress: float
# 0.0 = completely relaxed
# 0.5 = moderate stress
# 1.0 = panic / overload

    attention: float
    # Ability to sustain focus on the current task.
    # High attention compresses subjective time (flow state).
    # 0.0 -> completely distracted
    # 0.5 -> average focus
    # 1.0 -> deep uninterrupted concentration

    fatigue: float
     # Mental exhaustion accumulated over time.
    # Fatigue builds gradually and reduces cognitive performance.
    # 0.0 -> fully rested
    # 0.5 -> mentally tired
    # 1.0 -> cognitive exhaustion

    novelty: float
      # Degree of environmental novelty or unfamiliarity. Novel environments require more processing and often alter subjective time perception.
    # 0.0 -> completely familiar
    # 0.5 -> partially new
    # 1.0 -> entirely novel environment

    emotion: float
 # Emotional valence (not intensity).
    # Negative values represent unpleasant emotions,
    # positive values represent pleasant emotions.
    # -1.0 -> intense negative emotion
    #  0.0 -> emotionally neutral
    # +1.0 -> intense positive emotion

    effort: float
  # Mental effort currently being invested.
# Unlike attention, effort measures how hard the brain is working.
# High effort with low attention indicates struggling,
# while high effort with high attention indicates productive engagement.
#
# 0.0 -> effortless
# 1.0 -> maximum cognitive effort

    def clamp(self):
        """
        Keeps every variable inside realistic bounds.
        Prevents impossible values such as stress = 1.4.
        """

        self.stress = max(0.0, min(1.0, self.stress))
        self.attention = max(0.0, min(1.0, self.attention))
        self.fatigue = max(0.0, min(1.0, self.fatigue))
        self.novelty = max(0.0, min(1.0, self.novelty))
        self.emotion = max(-1.0, min(1.0, self.emotion))
        self.effort = max(0.0, min(1.0, self.effort))