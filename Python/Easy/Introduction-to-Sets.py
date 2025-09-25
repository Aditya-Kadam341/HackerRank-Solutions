n = int(input())
arr = list(map(int, input().split()))
addition=sum(set(arr))
count=len(set(arr))
total=addition/count
print(total)