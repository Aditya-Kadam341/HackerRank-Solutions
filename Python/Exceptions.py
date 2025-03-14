for i in range(int(input())):
    try : 
        n,m = map(int,input().split())
        print(n//m)
    except Exception as e:
        print("Error Code:",e)