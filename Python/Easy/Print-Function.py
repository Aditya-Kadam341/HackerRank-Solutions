# The included code stub will read an integer, n , from STDIN.
# Without using any string methods, if n = 5 then try to print the following:
# 12345 


n = int(input("Enter a number : "))
for i in range(1,n+1):
    print(i,end="")

