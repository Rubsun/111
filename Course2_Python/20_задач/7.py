from pprint import pprint

data = {i: round(i**0.5, 1) if i >= 0 else 'Ошибка' for i in range(-20, 21)}

data= {key: val for key, val in data.items() if isinstance(val, (int,float))}

data = {data[key] = val * 2 if '2' in str(val) else data[key] = val key: val for key, val in data.items()}

pprint(data)