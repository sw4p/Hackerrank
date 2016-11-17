n = int(input())
arr = [int(x) for x in input().split()]
max1 = -101
max2 = -102
for i in arr:
	if i > max1:
		max2 = max1
		max1 = i
	elif i > max2 and i < max1:
		max2 = i

print(max2)
