data = int(input())

if data % 2 != 0:
    print("Weird")
elif data % 2 == 0 and data in range(2,6):
    print("Not Weird")
elif data % 2 == 0 and data in range(6,21):
    print("Weird")
elif data % 2 == 0 and data > 20:
    print("Not Weird")
