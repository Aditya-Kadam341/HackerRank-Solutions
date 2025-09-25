# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

# If the number is in between 6-21 and is odd it is Weird. Else it is Not Weird

n = int(input("Enter a number : ").strip())
if (n in range(6,21) or (n%2 !=0)):
    print("Weird")
else:
    print("Not Weird")


