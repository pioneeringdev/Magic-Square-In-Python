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
            print('{:4d}'.format(magic_square[row][col]), end='')
        print("\n")

def main():
    print ("Enter the size of magic square:")

    while True:
        try:
            N = int(input())
            if N < 1:
                print("Pleae input positive number.")
            elif N%2 == 0:
                print("Please input odd number.")
            else:
                print_magic_square(calculate_matic_square(N))
                break
        except ValueError:
            print("Please input an integer.")

if __name__ == '__main__':
    main()
