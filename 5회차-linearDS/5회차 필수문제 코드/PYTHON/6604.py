n = int(input())
dic = {}
for i in range(n):
    now = input().split()
    dic[now[0]] = [now[1], now[2]]

while True:
    try:
        line = input()
        line = line.strip()
        ans = 0
        error = False
        stk = []
        for i in line:
            if i == '(':
                continue
            elif i == ')':
                b = list(map(int, stk.pop()))
                a = list(map(int, stk.pop()))
                
                if b[0] != a[1]:
                    error = True
                    break
                ans += a[0] * b[0] * b[1]
                stk.append([a[0], b[1]])
            else:
                stk.append(dic[i])

        if error:
            print("error")
        else:
            print(ans)
    except EOFError:
        break

