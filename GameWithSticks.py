n, m = map(int, input().split())

checkFlag = 0
intersectionList = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        intersectionList.append([i, j])

intersectionList.reverse()

while len(intersectionList) > 0:
    horizontalAxis, verticalAxis = intersectionList.pop()
    checkFlag += 1
    removeList = []
    for element in intersectionList:
        if element[0] == horizontalAxis or element[1] == verticalAxis:
            removeList.append(element)
    for ele in removeList:
        intersectionList.remove(ele)

if checkFlag % 2 != 0:
    print("Akshat")
else:
    print("Malvika")
