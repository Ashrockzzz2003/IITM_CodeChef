for _ in range(int(input())):
    xml = input()
    flag = 0
    ans = 0
    temp = 0
    for char in xml:
        if char == "<":
            flag += 1
        else:
            flag -= 1
            if flag < 0:
                break
            temp += 1
            if flag == 0:
                ans = temp*2
    
    print(ans)