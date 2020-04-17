n = int(input())
responseList = list(map(int, input().split()))
check = 0
for i in range(n):
    if responseList[i] == 1:
        check += 1
        break
if check == 0:
    print("EASY")
else:
    print("HARD")
