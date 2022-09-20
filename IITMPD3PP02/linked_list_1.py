class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getNthNodeFromEnd(head, n):
    temp_1 = head
    temp_2 = head
    for i in range(n):
        if temp_2 is None:
            return None
        temp_2 = temp_2.next
    while temp_2:
        temp_1 = temp_1.next
        temp_2 = temp_2.next
    return temp_1.data
