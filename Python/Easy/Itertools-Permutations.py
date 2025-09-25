from itertools import permutations
S,k = input().split(" ")
S = list(permutations(S,int(k)))
S.sort()
print(S)
for i in S:
    print("".join(i))