
import matplotlib.pyplot as plt
import numpy as np


def plot_time_perception(history):
    """
    Plot objective time against subjective time.
    """

    real_time = history["real_time"]

    plt.figure(figsize=(10, 5))

    plt.plot(
        real_time,
        history["perceived_time"],
        linewidth=2,
        label="Perceived Time"
    )

    plt.plot(
        real_time,
        real_time,
        "--",
        linewidth=2,
        label="Real Time"
    )

    plt.title("Subjective vs Objective Time")
    plt.xlabel("Real Time (seconds)")
    plt.ylabel("Elapsed Time (seconds)")
    plt.grid(True)
    plt.legend()


def plot_cognitive_state(history):
    """
    Plot all cognitive variables over time.
    """

    t = history["real_time"]

    plt.figure(figsize=(12, 6))

    plt.plot(t, history["stress"], label="Stress")
    plt.plot(t, history["attention"], label="Attention")
    plt.plot(t, history["fatigue"], label="Fatigue")
    plt.plot(t, history["novelty"], label="Novelty")
    plt.plot(t, history["effort"], label="Effort")
    plt.plot(t, history["emotion"], label="Emotion")

    plt.title("Evolution of Cognitive State")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Normalized Value")
    plt.ylim(-1.05, 1.05)
    plt.grid(True)
    plt.legend()


def plot_distortion(history):
    """
    Plot the subjective time distortion factor.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        history["real_time"],
        history["distortion"],
        linewidth=2
    )

    plt.title("Time Distortion Factor")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Distortion (×)")
    plt.grid(True)


def plot_phase_space(history):
    """
    Stress vs Attention phase-space trajectory.

    Color represents simulation progress.
    """

    attention = np.array(history["attention"])
    stress = np.array(history["stress"])

    colors = np.linspace(0, 1, len(attention))

    plt.figure(figsize=(8, 8))

    scatter = plt.scatter(
        attention,
        stress,
        c=colors,
        cmap="viridis",
        s=35,
        label="Trajectory"
    )

    plt.plot(
        attention,
        stress,
        alpha=0.4
    )

    # Start marker
    plt.scatter(
        attention[0],
        stress[0],
        s=150,
        marker="o",
        label="Start"
    )

    # End marker
    plt.scatter(
        attention[-1],
        stress[-1],
        s=180,
        marker="X",
        label="End"
    )

    plt.colorbar(scatter, label="Simulation Progress")

    plt.title("Cognitive Phase Space")
    plt.xlabel("Attention")
    plt.ylabel("Stress")

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.grid(True)
    plt.legend()


def plot_summary(history):
    """
    Generate every visualization for a simulation.
    """

    plot_time_perception(history)
    plot_cognitive_state(history)
    plot_distortion(history)
    plot_phase_space(history)

    plt.show()
