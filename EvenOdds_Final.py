n, k = map(int, input().split())

if n % 2 == 0:

    oddLen = (((n-1) - 1)/2) + 1
else:
    oddLen = ((n - 1) / 2) + 1

if k <= oddLen:
    result = 1 + 2 * (k-1)
else:
    result = 2 + 2 * (k - oddLen - 1)
print(int(result))