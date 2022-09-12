def count_boast(A):
    count = 0
    for i in range(len(A)):
        greater_than_ai = []
        for j in range(len(A)):
            if (i != j):
                if(A[j] > A[i]):
                    greater_than_ai.append(1)
        if (len(A) - len(greater_than_ai) - 1) >= (len(greater_than_ai)):
            count += 1
    
    return count
    
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split(' ')))
    print(count_boast(A))
