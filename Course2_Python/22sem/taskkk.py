from math import pi 
def get_degree(r: float, t: float, a:float, v:float):
    """
    Находит на какой градус изменилось расположении точки относитоельно стартовой точки
    """
    S = v*t + (a*(t**2)/2)
    C = 2*pi*r
    return round(((S%C)/ C* 360),3 )
print(get_degree(1.2, 13.2, 1.9, 19.2))


