# Lorenz-inspired Chaotic Finance Model

This repository contains a small project exploring **financial dynamics** through a **Lorenz-type nonlinear system**.  
The three state variables are interpreted as:

- `x`: net interest rate
- `y`: investment level
- `z`: physical stocks or financial reserves

By varying the parameters $(\sigma, \rho, \beta)$, we study:
- the **equilibria** of the system and their **stability**,
- **oscillatory** vs. **convergent** regimes,
- the emergence of **chaotic behaviour** and
- the **sensitivity to initial conditions** (hallmark of chaos).

A complementary written report (in French) also introduces a **Petri net model** for the budget of a student association, as a discrete-event counterpart to the continuous-time model.

---

## 1. Mathematical model

We consider the Lorenz system:
\[
\dot x = \sigma (y - x), \quad
\dot y = x(\rho - z) - y, \quad
\dot z = xy - \beta z,
\]
with:
- $x$ = net interest rate,
- $y$ = investment level,
- $z$ = stocks / financial reserves,
- $\sigma, \rho, \beta > 0$ parameters (Prandtl number, normalized Rayleigh number, geometric factor).

### Equilibria and stability

The model admits:
- The trivial equilibrium $E_0 = (0,0,0)$
- Two non-trivial equilibria $E_\pm$ (for $\rho > 1$):
\[
E_\pm = \big(\pm\sqrt{\beta(\rho-1)},\ \pm\sqrt{\beta(\rho-1)},\ \rho-1\big).
\]

We compute the **Jacobian** at these equilibria and analyse its **eigenvalues**.  
Using the **Routh–Hurwitz criterion**, we obtain parameter conditions for:
- stability of the origin $E_0$,
- stability of $E_\pm$,
- onset of oscillations and chaotic regimes.

For the full derivations and economic interpretation, see the report in `report/Rapport_Sujet12GrN_V2.pdf`.

---

## 2. Repository contents

### `src/modele_mod.py`

- Defines the Lorenz-type system with parameters `(sigma, rho, beta)`.
- Computes:
  - equilibrium points,
  - Jacobian matrix at equilibria,
  - eigenvalues and qualitative stability.
- Can be used to explore how the dynamics change when you move in the parameter space.

Main functions:
- `lorenz(t, variables, sigma, rho, beta)`: right-hand side of the ODE system.
- `resolution(...)`: solves the system using `scipy.integrate.solve_ivp` (RK45).
- `calcul_eq(sigma, rho, beta)`: returns the equilibrium points.
- `jacobienne(x, y, z, sigma, rho, beta)`: Jacobian at a given equilibrium.
- `stabilite(equilibre, sigma, rho, beta)`: basic stability analysis from eigenvalues.

### `src/finite_differences.py`

Educational implementation of the Lorenz system with a **homemade RK4 scheme**:

- Implements:
  - `lorenz_deriv(t, xyz, sigma, rho, beta)`,
  - `rk4(...)` for generic ODE integration,
  - `rk4_lorenz(...)` to simulate the full trajectory.

- Plots trajectories in the planes:
  - $(x, y)$
  - $(y, z)$
  - $(x, z)$

This script is mainly used to visualise the **Lorenz attractor** for classical parameters such as:
- $\sigma = 10$,
- $\rho = 28$,
- $\beta = 8/3$.

### `src/CI-difference.py`

Focuses on **sensitivity to initial conditions**:

- Simulates two trajectories with:
  - CI1 = (1.0, 1.0, 1.0)
  - CI2 = (1.01, 1.0, 1.0)
- Uses RK4 to integrate both trajectories on the same time grid.
- Plots the results in different planes to highlight how quickly the trajectories diverge.

This illustrates the **“butterfly effect”**: tiny perturbations at $t=0$ lead to very different long-term behaviours.

### `report/Rapport_Sujet12GrN_V2.pdf`

Written report (in French) with:

- **Context & motivation**: why chaotic models can be relevant for finance.
- **State of the art**: references on Lorenz attractor and chaotic finance.
- **Detailed analysis** of:
  - continuous-time model,
  - equilibria and their stability (mathematical + economic point of view),
  - numerical simulations (oscillations, convergence, chaos).
- **Petri net model** for the budget of a student association:
  - places = states of a project (submitted, validated, financed, etc.),
  - transitions = decisions (president, treasurer, VP relations entreprises),
  - shows how project funding flows through the association.

---

## 3. Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/lorenz-chaotic-finance.git
cd lorenz-chaotic-finance

