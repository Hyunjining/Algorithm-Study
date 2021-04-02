n = int(input())
stack = []
result = []
count = 1

for i in range(0,n):
    data = int(input())
    while(count<=data):
        stack.append(count)
        count = count + 1
        result.append('+')
    if(stack[-1]==data):
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))
