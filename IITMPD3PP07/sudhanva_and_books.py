try:
    import queue
    q = int(input())
    stack = queue.LifoQueue(maxsize=1000000000)
    while q != 0:
        x = [int(i) for i in input().split(' ')]
        if(len(x) == 2):
            stack.put(x[-1])
        else:
            if(stack.qsize() == 0):
                print("kuchbhi?")
            else:
                print(stack.get())
        q -= 1
except EOFError:
    pass