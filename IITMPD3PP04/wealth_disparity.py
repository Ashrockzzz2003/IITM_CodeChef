# A[i] -> Net wealth of ith employee
#      -> -ve if employee is in debt
"""
- identify a pair of employess i and j, j is a subordinate of i such that A[i] - 
  A[j] is maximum
- P[i] -> Parent of A[i]
"""

import sys
sys.setrecursionlimit(2**31 - 1)

def depth_first_search(root, x):
    result = x - A[root]
    x = max(x, A[root])
    for v in a_list[root]:
        result = max(result, depth_first_search(v, x))
    return result

x = list(map(int, input().split(' ')))

N = x[0]
A = x[1:N+1]
P = x[N+1:]

a_list = [[] for i in range(N)]

for i in range(N):
    if P[i] == -1:
        # Identifying root of graph
        hojo = i
    else:
        a_list[P[i] - 1].append(i)

print(depth_first_search(hojo, A[hojo]))
