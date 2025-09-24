import re
for i in range(int(input())):
    boo=True 
    try:
        reg=re.compile(input())
    except re.error:
        boo=False
    print(boo)
