# Enter your code here. Read input from STDIN. Print output to STDOUT#

from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)
for i in range (n):
    abn = input().strip()
    d[abn].append(i+1)
for j in range (m):
    abm = input().strip()
    if abm in d :
        print(" ".join(map(str,d[abm])))
    else:
        print("-1")



    

