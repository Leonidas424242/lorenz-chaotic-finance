import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Paramètres
sigma = 1.9
rho = 1.09
beta = 1.00


# condition de stabilité 
stabilite = beta * (rho + sigma) * (beta + sigma + 1) - 2 * beta * sigma * (rho - 1)

# Système d'équations différentielles
def lorenz(t, variables):
    x, y, z = variables
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Conditions initiale et temps
CI = [1,   1, 1]
tps = (0, 50)  # Intervalle de temps
division_temps = np.linspace(tps[0], tps[1], 10000)  # Points de temps pour l'évaluation

# Résolution du système
def résolution():
    solution = solve_ivp(lorenz, tps, CI, t_eval=division_temps, method='RK45')
    return solution

solution = résolution()

# Extraction des résultats
t = solution.t
x, y, z = solution.y

# graphe
plt.figure(figsize=(10, 6))
plt.plot(t, x, label="x (Taux d'intérêt net)", color='blue')
plt.plot(t, y, label="y (Investissement)", color='green')
plt.plot(t, z, label="z (Stocks)", color='red')
plt.xlabel("Temps", fontsize=12)
plt.ylabel("Valeurs des variables", fontsize=12)
plt.legend()
plt.grid()

# variables sur graph
text = (f"$\\sigma = {sigma}$\n"
        f"$\\rho = {rho}$\n"
        f"$\\beta = {beta:.2f}$\n"
        f"$\\beta (\\rho + \\sigma) (\\beta + \\sigma + 1) - 2\\beta\\sigma (\\rho - 1) = {stabilite:.2f}$")
plt.gcf().text(0.02, 0.95, text, fontsize=12, verticalalignment='top')

plt.tight_layout()
plt.show()

# Calcul points d'équilibre
def calcul_eq(sigma, rho, beta):
    if rho > 1:
        eq_plus = (np.sqrt(beta * (rho - 1)), np.sqrt(beta * (rho - 1)), rho - 1)
        eq_minus = (-np.sqrt(beta * (rho - 1)), -np.sqrt(beta * (rho - 1)), rho - 1)
        return [(0, 0, 0), eq_plus, eq_minus]
    else:
        return [(0, 0, 0)]

equilibre = calcul_eq(sigma, rho, beta)
print("\n Points d'équilibre:")
for eq in equilibre:
    print(eq)

# Analyse stabilité
def jacobienne(x, y, z, sigma, rho, beta):
    return np.array([
        [-sigma, sigma, 0],
        [rho - z, -1, -x],
        [y, x, -beta]
    ])

def stabilité(equilibre, sigma, rho, beta):
    for eq in equilibre:
        J = jacobienne(*eq, sigma, rho, beta)
        eigenvalues = np.linalg.eigvals(J)
        print(f"\n Point d'équilibre {eq}: Valeurs propres = {eigenvalues}")

stabilité(equilibre, sigma, rho, beta)