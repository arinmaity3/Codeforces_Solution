numOfCoins = int(input())
coinsList = list(map(int, (input().split())))

minResult = 0
share = 0

totalSum = sum(coinsList)

coinsList.sort()

while share <= totalSum/2:
    share += coinsList.pop()
    minResult += 1

print(minResult)
