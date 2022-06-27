## a line을 input으로 받아 list에 저장
# space를 기준으로 split함

if __name__ == '__main__':
    # raw_input(): always return string
    N = int(raw_input()) # the # of cmd 
    
    # result list
    arr = []
    
    # all N commands
    for line in range(N):
        # get user input (command) &
        # store a line as a list
        cmd = raw_input().split()
        
        # check what cmd will be executed
        if cmd[0] == "insert":
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(arr)
        elif cmd[0] == "remove":
            arr.remove(int(cmd[1]))
        elif cmd[0] == "append":
            arr.append(int(cmd[1]))
        elif cmd[0] == "sort":
            arr.sort()
        elif cmd[0] == "pop":
            arr.pop()
        elif cmd[0] == "reverse":
            arr.reverse()
        
