import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(history):
    """
    Animate the evolution of the simulation.
    """

    time = history["real_time"]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.set_xlim(0, max(time))
    ax.set_ylim(0, 1.1)

    ax.set_title("Dilate Cognitive State")
    ax.set_xlabel("Simulation Time (seconds)", fontsize=11)
    ax.set_ylabel("Normalized Cognitive State", fontsize=11)

    line_stress, = ax.plot([], [], label="Stress")
    line_attention, = ax.plot([], [], label="Attention")
    line_fatigue, = ax.plot([], [], label="Fatigue")

    ax.legend()

    def update(frame):

        x = time[:frame]

        line_stress.set_data(
            x,
            history["stress"][:frame]
        )

        line_attention.set_data(
            x,
            history["attention"][:frame]
        )

        line_fatigue.set_data(
            x,
            history["fatigue"][:frame]
        )

        return (
            line_stress,
            line_attention,
            line_fatigue,
        )

    anim = FuncAnimation(
        fig,
        update,
        frames=len(time),
        interval=40,
        blit=True,
        repeat=False,
    )

    plt.show()

    return anim