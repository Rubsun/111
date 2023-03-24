
def IsSymmetric(A):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
        return True


n = int(input())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(IsSymmetric(matrix))