nums = int(input())
numList = list(map(int, input().split()))

nonDecreasingSeg = 1
nonDecreasingSegList = []
startingPoint = numList[0]

for i in range(1, len(numList)):
    if numList[i] >= startingPoint:
        nonDecreasingSeg += 1
    else:
        nonDecreasingSegList.append(nonDecreasingSeg)
        nonDecreasingSeg = 1
    startingPoint = numList[i]

nonDecreasingSegList.append(nonDecreasingSeg)
print(max(nonDecreasingSegList))


