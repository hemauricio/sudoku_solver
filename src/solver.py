import settings

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

# Check if the number n can be placed in settings.data[y][x]
def possible(y, x, n):

    # Check horizontally and vertically respectively 
    for i in range(9):
        # If the number n is already in that row or column
        if settings.data[y][i] == n or settings.data[i][x] == n:
            return False
    
    # Check 3x3 square

    # We need to make sure our first square is divisible by 3
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            # Check the origin + 2 max in y and x
           if settings.data[y0 + i][x0 + j] == n:
               return False

    # If we can actually put the number there, just return True
    return True

def solve():

    # Traverse the matrix
    for i in range(9):
        for j in range(9):

            # 0 means blank space
            if settings.data[i][j] == 0:

                # Check if any number between 1 and 9 is a possible solution to that square
                for n in range(1, 10):
                    if possible(i, j, n):

                        # If it is, we put it there
                        settings.data[i][j] = n

                        # And call recursively with that possible solution
                        solve()

                        #If solve() with that solution didn't work, we backtrack and continue with the next number
                        settings.data[i][j] = 0

                # No possible solution here, just return
                # It's unreachable if we continuously have possible solutions
                return
            # We'll be here if there are no more 0's in the puzzle, so we just finished

    # We print our solution
    print('------- Solution -------')
    print(settings.data)

    # This return will backtrack to the recursive call above
    # In case there's more than 1 solution, this will print every solution
    return
