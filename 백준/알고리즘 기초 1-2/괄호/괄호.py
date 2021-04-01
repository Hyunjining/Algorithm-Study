N = int(input())

for j in range(0,N):
    ch = input()
    size = len(ch)
    num=0 
    for i in range(0,size):
        if ch[i]== '(':
            num = num+1
        else:
            num = num-1
        if num < 0:
            break
    if num==0:
        print("YES")
    else:
        print("NO")