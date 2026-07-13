from core.model import TimeModel
from core.dynamics import update_state


class Simulation:
    """
    Runs the Chrona cognitive simulation.

    Responsibilities:
    - Advance the cognitive state over time
    - Compute subjective time distortion
    - Record the complete simulation history
    """

    def __init__(
        self,
        initial_state,
        profile,
        duration=300,
        timestep=1
    ):

        self.state = initial_state
        self.profile = profile
        self.duration = duration
        self.timestep = timestep

        self.model = TimeModel()

        self.history = {
            "real_time": [],
            "perceived_time": [],
            "distortion": [],
            "stress": [],
            "attention": [],
            "fatigue": [],
            "novelty": [],
            "effort": [],
            "emotion": [],
        }

    def run(self):
        """
        Executes the simulation and returns the recorded history.
        """

        perceived_time = 0.0

        for second in range(0, self.duration, self.timestep):

            # Compute current subjective time distortion
            distortion = self.model.distortion(self.state)

            # Accumulate perceived time
            perceived_time += distortion * self.timestep

            # Record current state
            self.history["real_time"].append(second)
            self.history["perceived_time"].append(perceived_time)
            self.history["distortion"].append(distortion)

            self.history["stress"].append(self.state.stress)
            self.history["attention"].append(self.state.attention)
            self.history["fatigue"].append(self.state.fatigue)
            self.history["novelty"].append(self.state.novelty)
            self.history["effort"].append(self.state.effort)
            self.history["emotion"].append(self.state.emotion)

            # Advance simulation
            update_state(
                self.state,
                self.profile,
                self.timestep
            )

        return self.history

    def summary(self):
        """
        Returns useful summary statistics after a simulation.
        """

        return {
            "real_time": self.duration,
            "perceived_time": self.history["perceived_time"][-1],
            "average_distortion": (
                sum(self.history["distortion"])
                / len(self.history["distortion"])
            ),
            "peak_stress": max(self.history["stress"]),
            "peak_fatigue": max(self.history["fatigue"]),
            "peak_effort": max(self.history["effort"]),
            "final_attention": self.history["attention"][-1],
            "final_novelty": self.history["novelty"][-1],
            "final_emotion": self.history["emotion"][-1],
        }
