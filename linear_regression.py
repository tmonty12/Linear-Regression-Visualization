import numpy as np

def calculateConstants(points):
    A = []
    b = []
    for point in points:
       A.append([point[0], 1])
       b.append([point[1]])
    A = np.array(A)
    Ata = np.matmul(A.T, A)
    Atb = np.matmul(A.T, b)
    b = np.array(b)
    x = np.linalg.solve(Ata, Atb)
    return x

    