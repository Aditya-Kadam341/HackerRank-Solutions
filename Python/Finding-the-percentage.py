n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(query_name)
print("++++++++++++++++++")
query_scores=student_marks[query_name]
print(student_marks)
print("++++++++++++++++++")
print("%.2f"%(sum(query_scores)/len(query_scores)))