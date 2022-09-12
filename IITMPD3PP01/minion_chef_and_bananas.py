from math import ceil

def take_the_pile(middle, piles, H):
    count = 0
    for i in range(len(piles)):
        count += ceil(piles[i]/middle)
    
    return (count <= H)

t = int(input())

for _ in range(t):
	N, H = map(int,input().split(' '))
	piles = list(map(int, input().split(' ')))
	
	low = 1
	high = max(piles)
	
	# Binary Search for Answer
	while low < high:
		middle = low + (high - low) // 2
		
		if(take_the_pile(middle, piles, H)):
		    high = middle
		else:
		    low = middle + 1
	
	print(low)
