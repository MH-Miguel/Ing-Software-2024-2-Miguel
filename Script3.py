# Martínez Herrera Miguel Agustín
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)
x=np.linspace(0,20,100)

plt.plot(x,f(x))
plt.show()