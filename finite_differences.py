import numpy as np
import matplotlib.pyplot as plt

# définition du système de Lorenz
def lorenz_deriv(t, xyz, sigma=10.0, rho=28.0, beta=8/3):
    """
    étant donné l'état [x, y, z], la fonction renvoie les dérivées [dx/dt, dy/dt, dz/dt]
    for the Lorenz system:
      dx/dt = sigma*(y - x)
      dy/dt = x*(rho - z) - y
      dz/dt = x*y - beta*z
    t: temps (n'est pas utilisé explicitement ici)
    sigma, rho, beta: paramètres
    """
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x*(rho - z) - y
    dzdt = x*y - beta*z
    return np.array([dxdt, dydt, dzdt])

# Runge-Kutta du 4ème ordre
# **kwargs permet de faire passer des paramètres supplémentaires (beta, ro ...) à la fonction
def rk4(f, t, xyz, dt, **kwargs):
    """
    (t, xyz) -> (t + dt, xyz_new).
    f: function f(t, xyz, **kwargs) -> derivatives
    """
    k1 = f(t,        xyz,               **kwargs)
    k2 = f(t+dt/2.0, xyz + 0.5*dt*k1,    **kwargs)
    k3 = f(t+dt/2.0, xyz + 0.5*dt*k2,    **kwargs)
    k4 = f(t+dt,     xyz +     dt*k3,    **kwargs)

    xyz_nouveau = xyz + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return xyz_nouveau

def rk4_lorenz(xyz0, t0, tf, dt, sigma=10.0, rho=28.0, beta=8/3):
    """
    intègre le système de Lorenz de t0 à tf avec dt comme pas, utilisant rk4.
    La fonction retourne : 
      t_vals: tableau de temps
      xyz_vals: tableau de taille (len(t_vals), 3) des valeurs (x,y,z).
    """
    n_steps = int(np.floor((tf - t0)/dt))
    t_vals = np.linspace(t0, tf, n_steps+1)
    
    xyz_vals = np.zeros((n_steps+1, 3))
    xyz_vals[0,:] = xyz0
    
    for i in range(n_steps):
        t = t_vals[i]
        xyz_current = xyz_vals[i,:]
        xyz_next = rk4(
            f=lorenz_deriv, 
            t=t, 
            xyz=xyz_current, 
            dt=dt,
            sigma=sigma, rho=rho, beta=beta
        )
        xyz_vals[i+1,:] = xyz_next
    
    return t_vals, xyz_vals

#plot
if __name__ == "__main__":
    # Paramètres constants 
    sigma = 10.0
    rho   = 28.0
    beta  = 8.0/3.0
    
    # condition initiale choisie
    xyz0 = [1.0, 1.0, 1.0]  # =(x0, y0, z0)
    
    # intervalle de temps et pas
    t0 = 0.0
    tf = 40.0   # temps final
    dt = 0.01   # pas
    
    
    t_vals, sol = rk4_lorenz(
        xyz0, t0, tf, dt, 
        sigma=sigma, rho=rho, beta=beta
    )
    
    # extraction de x,y et z 
    x_vals = sol[:,0]
    y_vals = sol[:,1]
    z_vals = sol[:,2]
    
    # Plot projections 2D (x,y), (y,z), (x,z), (comme dans l'article)
    fig = plt.figure(figsize=(12,4))
    
    # plan XY
    ax1 = fig.add_subplot(1,3,1)
    ax1.plot(x_vals, y_vals, 'b-', linewidth=0.8)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('plan xy')
    
    # plan YZ
    ax2 = fig.add_subplot(1,3,2)
    ax2.plot(y_vals, z_vals, 'g-', linewidth=0.8)
    ax2.set_xlabel('y')
    ax2.set_ylabel('z')
    ax2.set_title('plan yz')
    
    # plan XZ
    ax3 = fig.add_subplot(1,3,3)
    ax3.plot(x_vals, z_vals, 'r-', linewidth=0.8)
    ax3.set_xlabel('x')
    ax3.set_ylabel('z')
    ax3.set_title('plan xz')
    
    plt.tight_layout()
    plt.show()