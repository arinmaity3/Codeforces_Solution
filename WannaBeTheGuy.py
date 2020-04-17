numOfLevels = int(input())
xList = list(map(int, input().split()))
yList = list(map(int, input().split()))

finalList = xList[1:] + yList[1:]

checkFlag = 0

for i in range(1, numOfLevels + 1):
    if finalList.count(i) == 0:
        checkFlag += 1
        break

if checkFlag == 0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")


