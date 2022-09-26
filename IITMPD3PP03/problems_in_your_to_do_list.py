T = int(input())

for _ in range(T):
    N = int(input())
    D = list(map(int, input().split(' ')))
    
    to_remove = 0
    for i in range(len(D)):
        if(D[i] >= 1000):
            to_remove += 1
            
    print(to_remove)
