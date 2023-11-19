import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)  
y = np.sin(x) 

plt.plot(x, y)  
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('نمودار تابع sin(x)')
plt.show()