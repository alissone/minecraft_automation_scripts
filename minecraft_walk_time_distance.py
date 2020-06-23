import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sympy.utilities.codegen import codegen
from sympy import symbols

# Read file 
df = pd.read_csv("minecraft_walk_time_distance.csv", header=None, comment="#")
df.columns = ["mode","time","x_delta","y_delta"]

# Convert columns
x_delta, y_delta = df["x_delta"].to_numpy(), df["y_delta"].to_numpy()
x_ax = df["time"].to_numpy()[:]
y_ax = np.sqrt(np.square(x_delta) + np.square(y_delta))[:]

# Calculate polynomial
z = np.polyfit(y_ax, x_ax, 4)
f = np.poly1d(z)
x_new = f(y_ax)

# Plot prediction
plt.style.use("ggplot")
plt.scatter(x=x_ax, y=y_ax)
plt.scatter(x_new, y_ax)
plt.show()

# Generate C code
distance = symbols('distance')
[(c_name, c_code), (h_name, c_header)] = \
codegen(('distance', f(distance)), "C99", "test",
         header=False, empty=False)
print(c_code)
