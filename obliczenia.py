import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

# --- CONFIGURATION ---
SPEED_FACTOR = 5  # Higher = Faster animation (skips more frames)
TOTAL_TIME = 10  # Seconds
POINTS = 3000  # High resolution for smooth curves


# --- FIELDS ---
def pole_elektryczne(t, r):
    return np.array([1.0, 0.0, 0.1])


def pole_magnetyczne(t, r):
    return np.array([0.0, t*1.0, 1.0])


# --- PHYSICS ---
def rownanie_ruchu(t, y, q, m):
    r = y[:3]
    v = y[3:]
    E = pole_elektryczne(t, r)
    B = pole_magnetyczne(t, r)
    F = q * (E + np.cross(v, B))
    a = F / m
    return np.concatenate((v, a))


# --- CALCULATION ---
print("Calculating trajectory...")
q, m = 1.0, 1.0
t_span = (0, TOTAL_TIME)
t_eval = np.linspace(0, TOTAL_TIME, POINTS)
y0 = np.array([0.0, 0.0, 0.0, 1.0, 0.5, 0.0])

sol = solve_ivp(
    fun=lambda t, y: rownanie_ruchu(t, y, q, m),
    t_span=t_span,
    y0=y0,
    t_eval=t_eval,
    method='RK45'
)

x_data, y_data, z_data = sol.y[0], sol.y[1], sol.y[2]

# --- ANIMATION SETUP ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Full Tail (Line)
line, = ax.plot([], [], [], lw=1, color='blue', alpha=0.5, label='Full Trajectory')
# 2. Particle (Head)
point, = ax.plot([], [], [], marker='o', color='red', markersize=4)

# Set fixed axes limits
margin = 2.0
ax.set_xlim(np.min(x_data) - margin, np.max(x_data) + margin)
ax.set_ylim(np.min(y_data) - margin, np.max(y_data) + margin)
ax.set_zlim(np.min(z_data) - margin, np.max(z_data) + margin)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Fast Particle Simulation (0-{TOTAL_TIME}s)')


def update(frame_idx):
    # Update the Full Tail (Always from 0 to current frame)
    line.set_data(x_data[:frame_idx], y_data[:frame_idx])
    line.set_3d_properties(z_data[:frame_idx])

    # Update the Head
    point.set_data([x_data[frame_idx]], [y_data[frame_idx]])
    point.set_3d_properties([z_data[frame_idx]])

    return line, point


# Create animation
# frames=range(...) skips data points to speed up visual playback
ani = FuncAnimation(
    fig,
    update,
    frames=range(0, len(t_eval), SPEED_FACTOR),
    interval=1,  # 1ms delay between frames (max speed)
    blit=False
)

plt.show()