def merge_lists(A, B):
  """Returns Sorted List of elements of A and B"""
  merged_list = []
  i, j, k = 0, 0, 0
  # i -> Pointer for A
  # j -> Pointer for B
  # k -> Pointer for the merged_list
  while k < (len(A) + len(B)): 
    # While there are elements to be merged
    if i == len(A): 
      # When A is empty
      merged_list.extend(B[j:])
      k += len(B) - j
    elif j == len(B):
      # When B is empty
      merged_list.extend(A[i:])
      k += len(A) - i
    
    # Compare top element of pile A with top element of pile B
    elif A[i] < B[j]:
      merged_list.append(A[i])
      i += 1
      k += 1
    else:
      merged_list.append(B[j])
      j += 1
      k += 1
  return merged_list

def merge_sort(L):
  """Returns Sorted List L using Merge Sort"""
  if len(L) <= 1:
    return L
  
  A = merge_sort(L[:(len(L))//2])
  B = merge_sort(L[len(L)//2:])

  merged_list = merge_lists(A, B)

  return merged_list

t = int(input())

for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    k = int(input()) # Position of playlist before sort
    # Each has unique positive integer length, it's enough to note the value and then trace it's location after a sort.
    # O(nlogn) solution I believe
    k = A[k-1] # Song length is k now.
    A = merge_sort(A)
    print(A.index(k) + 1)
