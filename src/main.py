import numpy as np
import settings
import solver

'''
--------x---------
5 3 0 0 7 0 0 0 0 |
6 0 0 1 9 5 0 0 0 |
0 9 8 0 0 0 0 6 0 |
8 0 0 0 6 0 0 0 3 |
4 0 0 8 0 3 0 0 1 y
7 0 0 0 2 0 0 0 6 |
0 6 0 0 0 0 2 8 0 |
0 0 0 4 1 9 0 0 5 |
0 0 0 0 8 0 0 7 9 |
'''

def main():

    settings.init()

    # Read values of our 9x9 board
    for i in range(9):
        aux = list(map(int, input().split()))
        settings.data.append(aux)

    # Convert to np array
    settings.data = np.array(settings.data)

    print('------- Input -------')
    print(settings.data)

    # Call our solve function
    solver.solve()


if __name__ == '__main__':
    main()

