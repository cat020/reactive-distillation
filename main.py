
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# Define constants
D = 10
a = 2.41
W_int = 100
x_w_int = 0.5

# Define time points for integration
t = np.linspace(0, 6, 100)  # Using more points for smoother plot

# Define the function for integration
def batch(x_w, t, D, a, W_int):
    W_t = -D * t + W_int
    y = a * x_w / (1.0 + x_w * (a - 1.0))
    dx_wdt = -(D / W_t) * (y - x_w)
    return dx_wdt

# Solve the ODE
x_w_sol = odeint(batch, x_w_int, t, args=(D, a, W_int))

# Plotting the solution
plt.figure()
plt.plot(t, x_w_sol, '-o')
plt.xlabel('Time, hours')
plt.ylabel('x_w')
plt.grid()
plt.show()
