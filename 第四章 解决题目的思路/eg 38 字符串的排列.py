from scipy.integrate import quad
import numpy as np


def function(t):
    return np.sin(t) / (np.pi - t)
result, error = quad(function, 0, np.pi)

print(f"数值解为：{result}")
print(f"估计误差为：{error}")
