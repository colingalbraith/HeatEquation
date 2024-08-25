# Heat Equation Simulation with Neumann Boundary Conditions

This simulation models heat conduction through a medium using the **heat equation** with Neumann boundary conditions. 
Below are some simulations with a constant forcing term in various locations:

Chess Board:
---

https://github.com/colingalbraith/HeatEquation/assets/146497900/81bd469e-12fa-4669-899f-43c6793b1abb

---

Grid of Dots:
---

https://github.com/colingalbraith/HeatEquation/assets/146497900/ae6cde21-6b81-4d25-b428-38a188eae25d

---

Random:
---

https://github.com/colingalbraith/HeatEquation/assets/146497900/27504756-5133-4c4c-b6d2-c120bd986e80

---

Center:
---

https://github.com/colingalbraith/HeatEquation/assets/146497900/d102656c-1935-4e6a-9179-d3f6dea37dde

---

Boundary:
---

https://github.com/colingalbraith/HeatEquation/assets/146497900/9e5c9e8a-a43a-42d0-a31d-0a6ba2edd6da

---

## Technical Overview


### Neumann Boundary Conditions
The Neumann boundary condition imposes that the gradient (or flux) of the temperature at the boundaries of the domain is zero. Mathematically, this means:
- \( \frac{\partial u}{\partial x} = 0 \) at the boundary for 1D.
- \( \frac{\partial u}{\partial x} = 0 \) and \( \frac{\partial u}{\partial y} = 0 \) at the boundary for 2D.

### Simulation Parameters
- **Thermal Diffusivity (`a`)**: Represents the heat diffusion coefficient. Higher values mean heat spreads faster through the medium.
- **Domain Length (`length`)**: The size of the domain (in mm) through which heat is conducted.
- **Time (`time`)**: The total duration (in seconds) for which the simulation runs.
- **Nodes (`nodes`)**: The number of discrete points in the simulation. Increasing the number of nodes improves accuracy but increases computation time.
- **Time Step (`dt`)**: Calculated to ensure stability in the simulation. Derived from the Courant-Friedrichs-Lewy (CFL) condition for numerical stability.
- **Forcing Term (`Q`)**: Represents a constant heat source added to the center of the domain to simulate external heating.

### 1D and 2D Simulations
The program simulates the heat equation in both 1D and 2D:

- **1D Simulation**: Models a single rod where heat is applied at the center and propagates outward, with insulated ends.
- **2D Simulation**: Models a flat plate where heat is applied at the center, and the temperature distribution evolves over time across the entire plate.

In both simulations, heat is initially distributed uniformly at 10°C. The forcing term (`Q`) applies heat to the center of the domain at each time step, raising the temperature locally.



### Visualizing the Simulation
The program visualizes the temperature distribution as it evolves over time. The plots are updated in real-time, showing:
- **1D Simulation**: A line plot that tracks temperature distribution along the rod over time.
- **2D Simulation**: A heatmap that tracks temperature distribution over the plate.

---

## Running the Simulation

To run the simulation, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/colingalbraith/HeatEquation.git
