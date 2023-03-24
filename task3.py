n = list(map(int, input().split()))
n.insert(0, n.pop()) #isert(куда нужно поместить, что нужно поместить). pop(-1 по умолчанию)
print(n)


#n = list(map(int, input().split()))#Ну или так, но срезы создают новую копию списка, что запрещено условием
#print(n[-1:]+n[:-1])