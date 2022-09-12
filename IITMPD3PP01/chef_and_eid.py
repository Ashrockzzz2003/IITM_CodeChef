t = int(input())

def find_min_diff(L):
    L.sort()
    X = []
    for i in range(len(L) - 1):
        X.append(abs(L[i] - L[i+1]))
    
    return min(X)

for _ in range(t):
    n = int(input())
    coin_list = list(map(int, input().split(' ')))
    print(find_min_diff(coin_list))
