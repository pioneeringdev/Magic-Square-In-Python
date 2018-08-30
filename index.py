# Create an N x N magic square. N must be odd.

def calculate_matic_square(N):
    N  = 5
    # magic_square = np.zeros((N,N), dtype=int)
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

    print(magic_square)

# def magic_square(my_matrix):
#     iSize = len(my_matrix[0])
#     sum_list = []
#
#     #Horizontal Part:
#     sum_list.extend([sum (lines) for lines in my_matrix])
#
#     #Vertical Part:
#     for col in range(iSize):
#         sum_list.append(sum(row[col] for row in my_matrix))
#
#     #Diagonals Part
#     result1 = 0
#     for i in range(0,iSize):
#         result1 +=my_matrix[i][i]
#     sum_list.append(result1)
#
#     result2 = 0
#     for i in range(iSize-1,-1,-1):
#         result2 +=my_matrix[i][i]
#     sum_list.append(result2)
#
#     if len(set(sum_list))>1:
#         return False
#     return True
#
# m=[[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
# print(magic_square_test(m));
#
# m=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# print(magic_square_test(m));
#
# m=[[2, 7, 6], [9, 5, 1], [4, 3, 7]]
# print(magic_square_test(m));
