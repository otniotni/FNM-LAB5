import numpy as np
import matplotlib.pylab as plt

def analytical_transmission_reflection():
    V0 = 1e5
    a = 0.04
    T = np.empty([])
    #observables = np.genfromtxt ("potential_well_default_observables.dat", dtype=float)
    E = np.array([k for k in range (150, 352, 2)])**2 / 2
    print(E)
    k1 = np.sqrt (2 * E)
    k2 = np.sqrt (2 * (E + V0))
    T = 1 / (1 + (k2**2 - k1**2)**2/(4*k1**2*k2**2)*np.sin (2*k2*a)**2)
    R = 1 - T
    print (R, T)
    return R, T


if __name__ == "__main__":
    R_ana, T_ana = analytical_transmission_reflection ()
    num_data = np.genfromtxt ("potential_well_RT_all.dat", dtype=float)
    k_num = num_data[:, 0]
    R_num = num_data[:, 1]
    T_num = num_data[:, 2]

    plt.figure()

    plt.plot (k_num, R_ana, label=r"$R_{ana}$")
    plt.plot (k_num, R_num, label=r"$R_{num}$")
    plt.plot (k_num, T_ana, label=r"$T_{ana}$")
    plt.plot (k_num, T_num, label=r"$T_{num}$")
    plt.xlabel (r"$k$")
    plt.legend()
    plt.show()
    