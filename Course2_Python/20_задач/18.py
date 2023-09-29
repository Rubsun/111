def sort_by_second(nested: list) -> list:
    """Сортирует по второму элементу, кто дал меньше - Прянишников"""
    return sorted(nested, key=lambda x: x[1])

print(sort_by_second([[1,2,3], [1,2]]))