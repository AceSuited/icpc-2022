n = int(input())
stk = [[] for _ in range(105)]

for i in range(n + 1):
    s = input()
    pos = 0
    for j in range(len(s)):
        if s[j] == ' ':
            stk[i].append(s[pos : j])
            pos = j + 1
    stk[i].append(s[pos:])

flag = True

while len(stk[n]) != 0:
    now = stk[n].pop()
    find = False
    for i in range(n):
        if len(stk[i]) == 0 or stk[i][-1] != now:
            continue

        stk[i].pop()
        find = True
    
    if find == False:
        flag = False
        break

if flag == True:
    print("Possible")
else:
    print("Impossible")
