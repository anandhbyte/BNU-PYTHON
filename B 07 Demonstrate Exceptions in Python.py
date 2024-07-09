# Import required libraries
import matplotlib.pyplot as plt

# This is our data
ages = [25, 22, 23, 23, 30, 31, 22, 35, 34, 56, 27, 45, 41, 19, 19, 26, 32, 33, 45, 40]

# Create histogram
plt.hist(ages, bins=5, edgecolor='black')

# Add title and labels
plt.title('Ages of Customers')
plt.xlabel('Age')
plt.ylabel('Number of Customers')

# Show the plot
plt.show()
