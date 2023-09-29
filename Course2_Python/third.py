# power = int(input())

# match power % 4:
#     case 0: print('1')
#     case 1: print('i')
#     case 2: print('-1')
#     case 3: print('-i')

# result = ['1','i','-1','-i']
print(['1','i','-1','-i'][int(input()) % 4])
