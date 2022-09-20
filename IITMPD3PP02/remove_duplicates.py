def binary_search(v, L):
    left = 0
    right = len(L) - 1
    
    if(len(L) == 0):
        return False
    
    while left <= right:
        middle = (left + right) // 2
        
        if(L[middle] == v):
            return True
        elif (L[middle] < v):
            left = middle + 1
        elif (L[middle] > v):
            right = middle - 1
    
    return False
        

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split(' ')))
    unique_list = []
    for i in A:
        if (binary_search(i, unique_list) == False):
            unique_list.append(i)
    for i in range(len(unique_list)):
        unique_list[i] = str(unique_list[i])
    print(" ".join(unique_list))
