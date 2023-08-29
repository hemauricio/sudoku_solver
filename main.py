import numpy as np

def solve():

    global data

    print(data)

    return

def main():

    global data 
    data = []

    for i in range(9):
        aux = list(map(int, input().split()))
        data.append(aux)

    data = np.array(data)

    # print(data)

    solve()


if __name__ == '__main__':
    main()

