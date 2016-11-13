n = int(input())
arr = list()
for i in range(0,n):
    command = input().split()
    if 'insert' in command:
        arr.insert(int(command[1]), int(command[2]))
    elif 'remove' in command:
        arr.remove(int(command[1]))
    elif 'append' in command:
        arr.append(int(command[1]))
    elif 'print' in command:
        print(arr)
    elif 'sort' in command:
        arr.sort()
    elif 'pop' in command:
        arr.pop()
    elif 'reverse' in command:
        arr.reverse()
