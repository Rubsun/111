mat = [0]
lenm = 1
num = int(input())


while len(mat) < num:
    for i in range(len(mat)):
        if mat[i] == 0:
            mat.append(1)
        else:
            mat.append(0)
#print(mat)
print(mat[:num])