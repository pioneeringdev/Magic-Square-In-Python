def calculate_matic_square(N):

    magic_square = [[0 for x in range(N)] for y in range(N)]
    n = 1
    i, j = 0, N//2

    while n <= N**2:
        magic_square[i][j] = n
        n += 1
        newi, newj = (i-1) % N, (j+1)% N
        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    return magic_square

def print_magic_square(magic_square):
    iSize = len(magic_square[0])
    for row in range(iSize):
        for col in range(iSize):
            print('{:5d}'.format(magic_square[row][col]), end='')
        print("\n")


def is_valid_magic_square(square_matrix):
    iSize = len(square_matrix[0])
    diagSum  = 0
    #prime diagonal some
    for i in range(iSize):
        diagSum += square_matrix[i][i]
    colSum = 0
    for col in range(iSize):
        colSum = 0
        for row in range(iSize):
            colSum += square_matrix[row][col]
        if colSum != diagSum:
            return False

    rowSum = 0;
    for row in range(iSize):
        rowSum = 0
        for col in range(iSize):
            rowSum += square_matrix[row][col]
        if rowSum != diagSum:
            return False
    return True

def main():
    print ("Enter the size of magic square:")

    while True:
        try:
            N = int(input())
            if N < 1:
                print("Pleae input positive odd number.")
            elif N%2 == 0:
                print("Please input odd number.")
            else:
                magic_square = calculate_matic_square(N)
                print_magic_square(magic_square)
                if is_valid_magic_square(magic_square):
                    print("Correct")
                else:
                    print("Incorrect")
                break
        except ValueError:
            print("Please input an integer.")


if __name__ == '__main__':
    main()
