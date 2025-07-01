import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y, label='Sine(x)', color='red', linestyle='--')
# plt.title('line Plot of Sin(x)')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.grid(True)
# plt.show()

# x = np.random.rand(50)
# y=np.random.rand(50)
# plt.scatter(x, y, color='blue', alpha=0.5)
# plt.title('Scatter Plot of Sin(x)')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# categories = ['A', 'B', 'C', 'D']
# values = [10, 20, 15, 25]   
# plt.bar(categories, values, color='green', alpha=0.7)
# plt.title('Bar Chart of Categories')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.show()

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=140,colors=['red','blue','green','yellow'],explode=(0.1,0,0,0),shadow=True)
plt.axis('equal')
plt.title('Pie Chart of Categories')
plt.show()