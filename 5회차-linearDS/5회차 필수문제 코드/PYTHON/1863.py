n = int(input())
stk = []
ans = 0

for i in range(n):
    a, b = map(int, input().split())

    if len(stk) == 0 or stk[-1] < b:
        stk.append(b)
    elif stk[-1] != b:
        while len(stk) != 0 and stk[-1] > b:
            stk.pop()
            ans += 1

        if len(stk) == 0 or stk[-1] < b:
            stk.append(b)

while len(stk) != 0:
    if stk[-1] != 0:
        ans += 1
    stk.pop()

print(ans)