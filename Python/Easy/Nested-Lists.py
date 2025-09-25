marksheet = []
scoresheet = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet +=[[name,score]]
    scoresheet += [score]
a = sorted(set(scoresheet))[1]

for i,j in sorted(marksheet):
    if a==j:
        print(i)