import matplotlib.pyplot
import numpy as numpy

# Define a range of x values
x = numpy.linspace(-10, 10, 100)

# Calculate the corresponding y values
y = 9 * x**2 - 5

# Plot the function
matplotlib.pyplot.plot(x, y)

# Add labels and title to the plot
matplotlib.pyplot.xlabel('x')
matplotlib.pyplot.ylabel('y')
matplotlib.pyplot.title('y = 9x^2 - 5')

# Show the plot
matplotlib.pyplot.show()