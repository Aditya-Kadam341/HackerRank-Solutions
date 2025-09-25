from collections import namedtuple
n=int(input())
data=namedtuple("data",input())
print(sum([int(data(*input().split()).MARKS)for i in range(n)])/n)
