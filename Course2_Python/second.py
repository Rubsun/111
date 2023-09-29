
def x_and_o(array: list) -> int:
    winner = 0
    side = 3
    for i in [1, -1]:
        main_d = 0
        second_d = 0
        # for j in range(3):
        #     if array[j][j] == i:
        #         mainD += 1
        #     if array[2-j][j] == i:
        #         secondD += 1
        main_d = len(set(array[j][j]
                     for j in range(side))) == 1 and array[0][0] == i
        second_d = len(set(array[j][side-1 - j]
                       for j in range(side))) == 1 and array[0][side-1] == i
        # row = 0
        # col = 0
        # for j in range(side):
        #     for k in range(side):
        #         if array[j][k] == i:
        #             row += 1
        #         if array[k][j] == i:
        #             col += 1
        row = True in [len(set(line)) == 1 and line[0] ==
                       i for line in list(zip(*array))]
        cols = True in [len(set(cols)) == 1 and cols[0] ==
                        i for cols in list(zip(*array))]

        if row == side or cols == side or main_d == side or second_d == side:
            winner += i
    return winner


array = [
    [1, 0, 0],
    [1, -1, 0],
    [1, -1, 0],
]
