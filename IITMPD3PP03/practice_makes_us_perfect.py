P = list(map(int, input().split(' ')))

count = 0

for i in range(len(P)):
    if(P[i] >= 10):
        count += 1

print(count)
