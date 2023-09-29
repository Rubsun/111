def theasure_map(map_tr: list) -> str:
    position_t = None
    position_x = None
    for i in range((len(map_tr))):
        for j in range(len(map_tr[i])):
            if map_tr[i][j] == 'x':
                position_x = [i, j]
            elif map_tr[i][j] == 't':
                position_t = [i, j]
    if not position_x or not position_t:
        return 'Not found'
        
    shift_x = position_t[1]- position_x[1]
    shift_y = position_t[0] - position_x[0]
    dir_x = 'W' if shift_x < 0 else 'E'
    dir_y = 'N' if shift_y < 0 else 'S'
    return dir_x*abs(shift_x)+dir_y*abs(shift_y)
     


print(theasure_map([
        ['x','','','','',''],
        ['','','','','',''],
        ['','','','','',''],
        ['','','','','',''],
        ['','','t','','',''],
]))

