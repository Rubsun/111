n = list(map(int, input().split()))
count = 0
count_answ = 0
for i in range(len(n)):
        for j in range(i):
            if n[i] == n[j]:
                count += 1

print(count)