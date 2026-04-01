"""
N-body gravitational simulation.
Simulates planets/stars attracting each other under gravity.
Run: python nbody.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 1.0          # gravitational constant (normalized units)
DT = 0.01        # time step
STEPS = 5000     # number of steps to simulate
TRAIL = 200      # trail length for visualization

# Initial conditions: [x, y, vx, vy, mass]
BODIES = [
    # Sun-like body at center
    [0.0,  0.0,  0.0,  0.0,  100.0],
    # Planets
    [1.0,  0.0,  0.0,  10.0,   1.0],
    [-1.5, 0.0,  0.0, -8.2,    1.0],
    [0.0,  2.0, -7.0,  0.0,    1.0],
    [2.5,  0.5,  1.0,  5.5,    0.5],
]

COLORS = ["gold", "steelblue", "tomato", "mediumseagreen", "orchid"]


def simulate(bodies):
    n = len(bodies)
    pos = np.array([[b[0], b[1]] for b in bodies], dtype=float)
    vel = np.array([[b[2], b[3]] for b in bodies], dtype=float)
    mass = np.array([b[4] for b in bodies], dtype=float)

    history = [pos.copy()]

    for _ in range(STEPS):
        acc = np.zeros_like(pos)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                r = pos[j] - pos[i]
                dist = np.linalg.norm(r) + 1e-5  # softening
                acc[i] += G * mass[j] * r / dist**3
        vel += acc * DT
        pos += vel * DT
        history.append(pos.copy())

    return np.array(history), mass


def main():
    print(f"Simulating {len(BODIES)} bodies for {STEPS} steps...")
    history, mass = simulate(BODIES)

    fig, ax = plt.subplots(figsize=(7, 7), facecolor="black")
    ax.set_facecolor("black")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("N-Body Simulation", color="white")

    n = len(BODIES)
    sizes = np.sqrt(mass) * 5
    dots = [ax.plot([], [], "o", color=COLORS[i % len(COLORS)], ms=sizes[i])[0] for i in range(n)]
    trails = [ax.plot([], [], "-", color=COLORS[i % len(COLORS)], alpha=0.3, lw=0.8)[0] for i in range(n)]

    def update(frame):
        start = max(0, frame - TRAIL)
        for i in range(n):
            dots[i].set_data([history[frame, i, 0]], [history[frame, i, 1]])
            trails[i].set_data(history[start:frame, i, 0], history[start:frame, i, 1])
        return dots + trails

    ani = animation.FuncAnimation(fig, update, frames=STEPS, interval=10, blit=True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
