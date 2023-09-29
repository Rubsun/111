odd = []
even = []
# for i in range(-10, 11, 2):
#     even.append(i)

# for i in range(-9, 11, 2):
#     odd.append(i)

for i in range(-10, 11):
    if i % 2 == 0:
        odd.append(i)
    else:
        even.append(i)

print(odd, even)
