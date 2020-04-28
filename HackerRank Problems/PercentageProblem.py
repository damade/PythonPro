n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if (query_name in student_marks.keys()):
    theList = student_marks[query_name]
    count = 0
    for i in range(len(theList)):
        count += theList[i]
    print(float(count / len(theList)))
else:
    print(f"{query_name} not found")
