A,B=map(int,input().split(' '))
for i in range (1,A,2):
    print((".|."*i).center(B,"-"))
print(("WELCOME").center(B,"-"))
for j in range (A-2,-1,-2):
    print((".|."*j).center(B,"-"))
