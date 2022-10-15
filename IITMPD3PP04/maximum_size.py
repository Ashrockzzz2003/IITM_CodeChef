import sys
sys.setrecursionlimit(2**31 - 1)

# [up, right, left, down]

directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

def depth_first_search(i, j, n, m, world_map):
    if i < 0 or j < 0 or i >= n or j >= m or world_map[i][j] == "0":
        return 0
    
    # Cell Visited
    world_map[i][j] = "0"
    
    no_of_ones = 1
    
    # Search All four directions
    for k in range(4):
        x = i + directions[k][0]
        y = j + directions[k][1]
        no_of_ones += depth_first_search(x, y, n, m, world_map)
    
    return no_of_ones

T = int(input())

for _ in range(T):
    n, m = map(int, input().split(' '))
    world_map = []
    for i in range(n):
        world_map.append(list(str(input())))
    
    moves = []
    
    for i in range(n):
        for j in range(m):
            if world_map[i][j] == "1":
                moves.append(depth_first_search(i, j, n, m, world_map))
    
    chef_count = 0
    moves.sort(reverse = True)
    for i in range(1, len(moves), 2):
        chef_count += moves[i]
    
    print(chef_count)
