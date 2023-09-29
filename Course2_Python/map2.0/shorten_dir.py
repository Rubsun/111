

def shorten_direction(dirs: str) -> str:
    back_dirs = {
        'W':'E',
        'E':'W',
        'S':'N',
        'N':'S',
    }
    result = []
    for value in dirs:
        if result and result[-1] == back_dirs[value]:
            result.pop()
        else:
            result.append(value)
    return ''.join(result)

print(shorten_direction('NESNWN'))