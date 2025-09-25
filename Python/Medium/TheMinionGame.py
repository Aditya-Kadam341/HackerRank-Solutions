def minion_game(string):
    # your code goes here
    l=len(string)
    consonants,vowels=0,0
    
    for i in range(l):
        if string[i] in "AEIOU":
            vowels=vowels+(l-i)
        else:
            consonants=consonants+(l-i)
    if consonants > vowels :
        print("Stuart",consonants)
    elif consonants==vowels:
        print("Draw")
    else:
        print("Kevin",vowels)
           

if __name__ == '__main__':
    s = input()
    minion_game(s)