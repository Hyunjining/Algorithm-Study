import sys
t = -1
stack = []

N = int(input())
for i in range(0, N):
    data = list(map(str,sys.stdin.readline().split()))
    if data[0] == "pop":
        if t == -1:
            print(-1)
        else:
            t = t-1
            print(stack[t+1])
            del stack[t+1]

    elif data[0] == "size":
        print(t+1)

    elif data[0] == "empty":
        if t == -1:
            print(1)
        else:
            print(0)

    elif data[0] == "top":
        if(t==-1):
            print(-1)
        else:
            print(stack[t])
    else:                   #push   
        t = t+1
        stack.append(int(data[1]))

