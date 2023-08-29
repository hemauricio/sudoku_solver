import numpy as np
import settings
import solver

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

