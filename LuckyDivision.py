number = int(input())
luckyNumberList = []
checkFlag = 0
for i in range(number+1):
    flag = 0
    for j in ["0", "1", "2", "3", "5", "6", "8", "9"]:
        if str(i).count(j) > 0:
            flag += 1
            if flag >= 1:
                break
    if flag == 0:
        luckyNumberList.append(i)

for k in luckyNumberList:
    if number % k == 0:
        checkFlag += 1
        print("YES")
        break

if checkFlag == 0:
    print("NO")







