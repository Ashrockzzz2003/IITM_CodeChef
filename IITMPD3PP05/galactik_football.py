from collections import defaultdict

MAXINT = float('inf')

n, m = list(map(int,input().split()))
(min_cost, cost) = ([], [-1])

graph = defaultdict(list)

for data in range(m):
    u, v = list(map(int, input().split()))
    # Add Edges
    graph[u].append(v)
    graph[v].append(u)

for data in range(n): 
    c = int(input())
    
    if c < 0:
        c = MAXINT
    cost.append(c)

ans = 0
visited = [False]*(n+1)

def dfs(k):
    m_cost = MAXINT
    q = [k]
    while q:
        v = q.pop()
        m_cost = min(m_cost, cost[v])
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    return m_cost

for u in range(1, n+1):
    if not visited[u]:
        visited[u] = True
        min_cost.append(dfs(u))

c_max = max(min_cost) 
c_min = min(min_cost)

if len(min_cost) == 1: 
    print(0)
    
elif c_max == MAXINT: 
    print(-1)
    
else: 
    print(sum(min_cost) + (len(min_cost) - 2)*c_min) 
    