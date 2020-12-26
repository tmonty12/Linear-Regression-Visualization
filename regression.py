from constants import calculate_constants
import matplotlib.pyplot as plt
import numpy as np

def regression():
    coords = [ ] 

    n = int(input("Enter number of coordinates : ")) 
    
    for i in range(0, n): 
        coord = [int(input("x: ")), int(input("y: "))] 
        coords.append(coord) 

    x_coords = []
    y_coords = []

    for coord in coords:
        x_coords.append(coord[0])
        y_coords.append(coord[1])
        
    constants = calculate_constants(coords)
    c = round(constants[0,0], 3)
    b = round(constants[1,0], 3)

    x = np.linspace(x_coords[0], x_coords[-1], len(x_coords))
    y = c*x + b

    plt.plot(x_coords, y_coords, 'o', label='Data points', color='blue')
    plt.plot(x, y, label='Linear Regression Line', color='orange')

    plt.legend()
    plt.show()