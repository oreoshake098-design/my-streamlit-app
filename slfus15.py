import numpy as np 
import matplotlib.pyplot as plt 
x = np.linspace(-10, 10, 100) 
# y = x² 
y = x ** 2 
plt.plot(x, y) 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.title("y = x²") 
plt.grid() 
plt.show()
#another example:sine funtion
import numpy as np 
import matplotlib.pyplot as plt 
x = np.linspace(0, 2 * np.pi, 100) 
y = np.sin(x) 
plt.plot(x, y) 
plt.xlabel("X") 
plt.ylabel("sin(X)") 
plt.title("Sine Function") 
plt.grid() 
plt.show()