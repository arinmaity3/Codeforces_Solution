limak, bob = map(int, input().split())

year = 0
while limak <= bob:
    limak = limak*3
    bob = bob*2
    year +=1

print(year)