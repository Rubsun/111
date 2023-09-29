def digits_to_spaces(text: str) -> str:
    return ''.join([' ' * int(c) if c.isdigit() else c for c in text ])
    res = ''
    for c in text:
        if c.isdigit():
            res += ' '*int(c)
        else:
            res += c
    return res

print(digits_to_spaces('a1bdcd3ef'))