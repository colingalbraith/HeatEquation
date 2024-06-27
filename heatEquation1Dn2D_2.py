import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numba import njit


matplotlib.use('TkAgg')


@njit
def simulate_1d(a, length, time, nodes, dt):
   # Initialization
   dx = length / nodes
   u = np.zeros(nodes) + 20  # Plate is initially at 20 degrees C


   # Boundary Conditions
   u[0] = 100
   u[-1] = 100


   # Simulating
   results = []
   counter = 0
   while counter < time:
       w = u.copy()
       u[1:-1] = dt * a * (w[:-2] - 2 * w[1:-1] + w[2:]) / dx**2 + w[1:-1]
       counter += dt
       results.append(u.copy())


   return results, np.arange(0, time, dt)


@njit
def simulate_2d(a, length, time, nodes, dt):
   # Initialization
   dx = length / nodes
   u = np.zeros((nodes, nodes)) + 20  # Plate is initially at 20 degrees C


   # Boundary Conditions
   u[0, :] = 100
   u[-1, :] = 100
   u[:, 0] = 100
   u[:, -1] = 100


   # Simulating
   results = []
   counter = 0
   while counter < time:
       w = u.copy()
       u[1:-1, 1:-1] = dt * a * (
           (w[:-2, 1:-1] - 2 * w[1:-1, 1:-1] + w[2:, 1:-1]) / dx**2 +
           (w[1:-1, :-2] - 2 * w[1:-1, 1:-1] + w[1:-1, 2:]) / dx**2
       ) + w[1:-1, 1:-1]
       counter += dt
       results.append(u.copy())


   return results, np.arange(0, time, dt)


def main():
   # Shared problem definition
   a = 110  # heat coefficient
   length = 50  # mm
   time = 8  # seconds
   nodes = 50


   dt_common = min(0.5 * (length / nodes) ** 2 / a, (length / nodes) ** 2 / (4 * a))


   # Run simulations
   results_1d, times_1d = simulate_1d(a, length, time, nodes, dt_common)
   results_2d, times_2d = simulate_2d(a, length, time, nodes, dt_common)


   # Set up plots
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
   pcm1 = ax1.pcolormesh([results_1d[0]], cmap=plt.cm.jet, vmin=0, vmax=100)
   ax1.set_ylim([-2, 3])
   ax1.set_title("1D Distribution")


   pcm2 = ax2.pcolormesh(results_2d[0], cmap=plt.cm.jet, vmin=0, vmax=100)
   ax2.set_title("2D Distribution")


   plt.ion()  # Turn on interactive mode


   for u1d, u2d, t in zip(results_1d, results_2d, times_1d):
       pcm1.set_array([u1d])
       ax1.set_title(f"1D Distribution at t: {t:.3f} [s].")


       pcm2.set_array(u2d)
       ax2.set_title(f"2D Distribution at t: {t:.3f} [s].")


       plt.pause(0.01)


   plt.ioff()  # Turn off interactive mode
   plt.show()


if __name__ == "__main__":
   main()

