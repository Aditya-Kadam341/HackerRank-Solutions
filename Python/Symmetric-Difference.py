# a = int(input())
# Set_A =input().split()
# b = int(input())
# Set_B = input().split()
# Set_A=set(Set_A)
# Set_B=set(Set_B)
# A_diff_B=Set_A.difference(Set_B)
# B_diff_A=Set_B.difference(Set_A)
# diff_union=sorted(A_diff_B.union(B_diff_A),key=int)
# print(Set_A)
# print(Set_B)
# print(A_diff_B)
# print(B_diff_A)
# print("\n".join(diff_union))



############# Different of doing it but same output ##########

a,Set_A = (int(input()), input().split())
b,Set_B = (int(input()), input().split())
Set_A=set(Set_A)
Set_B=set(Set_B)
A_diff_B = Set_A.difference(Set_B)
B_diff_A = Set_B.difference(Set_A)
diff_union = A_diff_B.union(B_diff_A)
print("\n".join(sorted(diff_union,key=int)))