n = int(input())
arr = input().split()
for i in range(0, n):
    arr[i] = int(arr[i])
arr = tuple(arr)
print(hash(arr))
