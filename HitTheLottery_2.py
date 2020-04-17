totalsum = int(input())

bill = 0

while totalsum > 0:
    if totalsum >= 100:
        bill += int(totalsum/100)
        totalsum %= 100
    elif totalsum >= 20:
        bill += int(totalsum/20)
        totalsum %= 20
    elif totalsum >= 10:
        bill += int(totalsum/10)
        totalsum %= 10
    elif totalsum >= 5:
        bill += int(totalsum/5)
        totalsum %= 5
    else:
        totalsum -= 1
        bill += 1

print(bill)
