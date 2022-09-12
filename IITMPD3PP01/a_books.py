t = int(input())

def find_count(A, i):
    count = 0
    for j in range(i+1, len(A)):
        if A[j] > A[i]:
            count += 1
    
    return str(count)

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split(' ')))
    B = []
    for i in range(len(A)):
        B.append(find_count(A, i))
    print(" ".join(B))
    
