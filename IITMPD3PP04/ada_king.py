T = int(input())

for _ in range(T):
    r, c, k = map(int, input().split(' '))
    possible_left = max(c - k, 1)
    possible_right = min((c + k), 8)
    possible_up = max((r - k), 1)
    possible_down = min((r + k), 8)
    
    w = possible_right - possible_left + 1
    l = possible_down - possible_up + 1
    
    # Area that can be covered = l*w
    print(l*w)
