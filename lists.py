if __name__ == '__main__':
    
    listInit = []
    
    n = int(input())
    
    
    
    for i in range(n):
        cmd = input().split()
        
        if cmd[0] == "insert":
            listInit.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "print":
            print(listInit)
        elif cmd[0] == "remove":
            listInit.remove(int(cmd[1]))
        elif cmd[0] == "append":
            listInit.append(int(cmd[1]))
        elif cmd[0] == "sort":
            listInit.sort()
        elif cmd[0] == "pop":
            listInit.pop()
        else:
            listInit.reverse()
