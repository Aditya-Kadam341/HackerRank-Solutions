from collections import Counter

X = int(input())
sizes = list(map(int,input().split(" ")))
N = int(input())
Dic = Counter(sizes)
total = 0
for i in range (N) :
    size,price = map(int,input().split(" "))
    if Dic[size]:
        Dic[size]-=1
        total+=price
print(total)