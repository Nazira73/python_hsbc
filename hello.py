# create a plot for the function f(x) = x^2
import matplotlib.pyplot as plt
import numpy as np
import json

x = np.linspace(-10, 10, 100)
# y = x**3
y = x**3


plt.plot(x, y)
plt.title('Plot of f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')  
plt.grid()
plt.savefig('plot.png')
plt.show()
# The plot is saved as 'plot.png'
# You can view it in the current directory.
# The plot is displayed using plt.show()
# The plot is displayed using plt.show()

# Read a JSON file and print its contents
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)