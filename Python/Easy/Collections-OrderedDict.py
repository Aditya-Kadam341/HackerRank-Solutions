from collections import OrderedDict

ordered_dictionary = OrderedDict()
n=int(input())
for i in range(n): 
    item_name , empty_space , item_price = input().rpartition(" ")
    # print("item_name" , item_name, "item_price", item_price)
    if item_name not in ordered_dictionary:
        ordered_dictionary[item_name] = int(item_price)
    else : 
        ordered_dictionary[item_name]+= int(item_price)

print(ordered_dictionary)
for i in ordered_dictionary.items() :
    print(*i)