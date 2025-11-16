import numpy as np
import matplotlib.pyplot as plt

# ce script permet de comparer les trajectoires partant de deux conditions initiales très voisines.

def lorenz(t, Y, sigma=10.0, rho=28.0, beta=8.0/3.0):
    
    x, y, z = Y
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])


def rk4(f, t0, y0, t_end, h, **kwargs):

    n_steps = int(np.ceil((t_end - t0) / h))
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros((n_steps + 1, len(y0)))
    
    # Initialisation
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(n_steps):
        t = t_values[i]
        y = y_values[i]
        
        k1 = f(t, y, **kwargs)
        k2 = f(t + 0.5*h, y + 0.5*h*k1, **kwargs)
        k3 = f(t + 0.5*h, y + 0.5*h*k2, **kwargs)
        k4 = f(t + h,    y + h*k3,     **kwargs)
        
        y_values[i+1] = y + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)
        t_values[i+1] = t + h
    
    return t_values, y_values


def main():
    # Paramètres
    t0 = 0.0
    t_end = 50.0
    h = 0.01
    sigma = 10.0
    rho = 28.0
    beta = 8.0/3.0
    
    # Deux conditions initiales proches
    y0_1 = np.array([1.0, 1.0, 1.0])
    y0_2 = np.array([1.01, 1.0, 1.0])
    
  
    t_vals1, sol1 = rk4(lorenz, t0, y0_1, t_end, h, sigma=sigma, rho=rho, beta=beta)
    t_vals2, sol2 = rk4(lorenz, t0, y0_2, t_end, h, sigma=sigma, rho=rho, beta=beta)
    
   
    x1, y1, z1 = sol1[:,0], sol1[:,1], sol1[:,2]
    x2, y2, z2 = sol2[:,0], sol2[:,1], sol2[:,2]
    

    fig = plt.figure(figsize=(12, 4))
    
    # (x, y)
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.plot(x1, y1, label='(1,1,1)')
    ax1.plot(x2, y2, label='(1.01,1,1)')
    ax1.set_title("Plan (x, y)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.legend()
    
    # (y, z)
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.plot(y1, z1, label='(1,1,1)')
    ax2.plot(y2, z2, label='(1.01,1,1)')
    ax2.set_title("Plan (y, z)")
    ax2.set_xlabel("y")
    ax2.set_ylabel("z")
    ax2.legend()
    
    # (z, x)
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.plot(z1, x1, label='(1,1,1)')
    ax3.plot(z2, x2, label='(1.01,1,1)')
    ax3.set_title("Plan (z, x)")
    ax3.set_xlabel("z")
    ax3.set_ylabel("x")
    ax3.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()