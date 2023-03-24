def can_eat(horse, figure):
    x1,y1,x2,y2 = 0,0,0,0
    x1,y1 = horse
    x2,y2 = figure
    if (abs(x1-x2)) == 1 and (abs(y1 - y2) == 2) or (abs(x2-x1)) == 2 and (abs(y2 - y1) == 1):
        return "resutl = True"
    return "result = False"

print(can_eat((int(input()), int(input())), (int(input()), int(input()))))
