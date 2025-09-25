def merge_the_tools(string, k):
    # your code goes here
    count=0
    empty_string=""
    for i in string:
        if i not in empty_string:
            empty_string+=i
        count+=1
        if count==k:
            print(empty_string)
            count=0
            empty_string=""


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)