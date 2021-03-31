N = int(input())

for i in range(0,N):
    ch = input()
    c_list = list(ch.split(' '))
    size = len(c_list)
    for i in range(0,size):
        c_list[i]=''.join(reversed(c_list[i]))
    print(' '.join(c_list))

