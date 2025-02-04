String = input("enter a string : ")            # ABCDCDC
Sub_String = input("enter a sub string : ")    # CDC
Count = 0

for i in range (0,len(String)):
    if String[i:].startswith(Sub_String):
        Count +=1

print(Count)