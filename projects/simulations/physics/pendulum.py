"""
Double pendulum simulation — a classic example of chaotic motion.
Run: python pendulum.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Parameters
G = 9.81      # gravity (m/s^2)
L1 = 1.0      # length of arm 1 (m)
L2 = 1.0      # length of arm 2 (m)
M1 = 1.0      # mass of bob 1 (kg)
M2 = 1.0      # mass of bob 2 (kg)
T_MAX = 20    # simulation time (seconds)
DT = 0.02     # time step


def equations(t, y):
    th1, w1, th2, w2 = y
    d = th2 - th1
    denom1 = (M1 + M2) * L1 - M2 * L1 * np.cos(d) ** 2
    denom2 = (L2 / L1) * denom1

    dw1 = (
        M2 * L1 * w1**2 * np.sin(d) * np.cos(d)
        + M2 * G * np.sin(th2) * np.cos(d)
        + M2 * L2 * w2**2 * np.sin(d)
        - (M1 + M2) * G * np.sin(th1)
    ) / denom1

    dw2 = (
        -M2 * L2 * w2**2 * np.sin(d) * np.cos(d)
        + (M1 + M2) * G * np.sin(th1) * np.cos(d)
        - (M1 + M2) * L1 * w1**2 * np.sin(d)
        - (M1 + M2) * G * np.sin(th2)
    ) / denom2

    return [w1, dw1, w2, dw2]


def main():
    t_span = (0, T_MAX)
    t_eval = np.arange(0, T_MAX, DT)

    # Initial conditions: [theta1, omega1, theta2, omega2] in radians
    y0 = [np.pi / 2, 0, np.pi / 2 + 0.01, 0]

    print("Solving...")
    sol = solve_ivp(equations, t_span, y0, t_eval=t_eval, method="RK45", rtol=1e-8)

    th1, th2 = sol.y[0], sol.y[2]
    x1 = L1 * np.sin(th1)
    y1 = -L1 * np.cos(th1)
    x2 = x1 + L2 * np.sin(th2)
    y2 = y1 - L2 * np.cos(th2)

    # Animate
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.set_title("Double Pendulum")
    ax.axis("off")

    line, = ax.plot([], [], "o-", lw=2, markersize=8, color="steelblue")
    trace, = ax.plot([], [], ",", color="salmon", alpha=0.4)
    trace_x, trace_y = [], []

    def update(i):
        trace_x.append(x2[i])
        trace_y.append(y2[i])
        line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
        trace.set_data(trace_x, trace_y)
        return line, trace

    ani = animation.FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
