import numpy as np

import matplotlib.pyplot as plt

# Example 1: Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Line Plot Example')
plt.legend()
plt.show()

# Example 2: Scatter plot
x = np.random.rand(100)
y = np.random.rand(100)

plt.figure()
plt.scatter(x, y, color='r', label='Random Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Example')
plt.legend()
plt.show()

# Example 3: Histogram
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='g')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()

# Example 4: Bar plot
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.figure()
plt.bar(categories, values, color='b')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot Example')
plt.show()