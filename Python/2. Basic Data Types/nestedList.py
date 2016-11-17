n = int(input())
student = []
for i in range(n):
	student.append([input(), float(input())])

sorted_marks = sorted(student, key = lambda x: x[1])
min1 = sorted_marks[0][1]

for i in range(n):
	if sorted_marks[i][1] > min1:
		min2 = sorted_marks[i][1]
		break

ans = []
for i in range(n):
	if sorted_marks[i][1] > min2:
		break
	elif sorted_marks[i][1] == min2:
		ans.append(sorted_marks[i][0])

ans_sorted = sorted(ans, key = str.lower)		
print(*ans_sorted, sep = '\n')
