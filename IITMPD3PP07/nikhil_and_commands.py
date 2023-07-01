for _ in range(int(input())):
    n = int(input())
    directory_list = []
    answers = []
    count = 0
    
    for i in range(n):
        cmd = input()
        if cmd[:3] == "pwd":
            result = "/".join(directory_list)
            if result == "":
                count += 1
                answers.append("/")
            else:
                count += 1
                answers.append("/" + result + "/")
            continue
        
        cmd = cmd[3:]
        if cmd[0] == "/":
            directory_list = []
            cmd = cmd[1:]
        if cmd[-1] == "/":
            cmd = cmd[:-1]
        
        instructions = cmd.split("/")
        
        for instruction in instructions:
            if instruction == "..":
                directory_list.pop()
            else:
                directory_list.append(instruction)
    
    for answer in answers:
        print(answer)