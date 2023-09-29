sting1 = input()
len_String = len(sting1) - len(sting1.replace('f', '')) #чтобы узнать кол-во F в стркое, нужно из исходной длинны 
if len_String == 0:
    print("В слове нет букв f")
elif len_String == 1:
    print(sting1.index('f'))
elif len_String >1:
    print(sting1.index('f'), sting1.rindex('f')) #rindex - возврашает набибольший индекс в строке