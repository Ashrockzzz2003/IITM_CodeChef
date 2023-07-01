import queue

def BFS(begin, end, distance, adj, s):
    
    vis = queue.Queue()
    vis.put(begin)

    distance[begin] = 0

    while vis.qsize() > 0:
        ind = vis.get()

        if ind > 0 and distance[ind - 1] == -1:
            distance[ind - 1] = distance[ind] + 1
            vis.put(ind - 1)

        if ind < len(s) - 1 and distance[ind + 1] == -1:
            distance[ind + 1] = distance[ind] + 1
            vis.put(ind + 1)

        for v in adj[s[ind]]:
            if distance[v] == -1:
                distance[v] = distance[ind] + 1
                vis.put(v)

        adj[s[ind]].clear()

    return dist[end]


s = [int(x) for x in input().strip()]
N = len(s)

dist = [-1 for _ in range(N)]
adj = [[] for _ in range(10)]

for i in range(N):
    adj[s[i]].append(i)

print(BFS(0, N - 1, dist, adj, s))