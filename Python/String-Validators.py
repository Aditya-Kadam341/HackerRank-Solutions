s = input("Enter Something : ")     # qA2
print(any(i.isalnum()for i in s))
print(any(i.isalpha()for i in s))
print(any(i.isdigit()for i in s))
print(any(i.islower()for i in s))
print(any(i.isupper()for i in s))