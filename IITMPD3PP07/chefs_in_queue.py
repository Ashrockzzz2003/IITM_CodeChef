n, k = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

x = 1
s = [[arr[-1], 1]]
j = 1

for i in range(n - 2, -1, -1):
    j += 1
    while s[-1][0] >= arr[i]:
        s.pop()
        if s == []:
            break
    
    if s != []:
        x *= (j - s[-1][1] + 1)
        x %= (10**9 + 7)
    
    s.append([arr[i], j])

print(x%(10**9+7))