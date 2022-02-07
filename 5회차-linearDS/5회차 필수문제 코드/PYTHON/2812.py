n, k = map(int, input().split())
s = input()

stk = []
cnt = 0
for i in range(len(s)):
    now = int(s[i])
    if len(stk) == 0 or stk[-1] >= now:
        stk.append(now)
    else:
        while len(stk) != 0 and stk[-1] < now and cnt < k:
            stk.pop()
            cnt += 1
        stk.append(now)

while cnt < k:
    stk.pop()
    cnt += 1

for it in stk:
    print(it , end="")