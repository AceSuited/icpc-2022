import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
M = 1000000007
datas = []
for i in range(n):
    datas.append(list(map(int,input().split())))

for data in datas:
    if data[0] == 0:
        continue
    if data[1] == 0:
        data[0] = 0
        continue
    data[0] = (data[0] % M) * (data[1] % M) % M
    data[1] -= 1



def pow(p):
    if p == 0:
        return 1 % M
    else:
        temp = pow(p // 2)
        if p % 2 == 0:
            return (temp * temp) % (M)
        elif p % 2 != 0:
            return (temp * temp * 2) % (M)



res = 0
for data in datas:
    if data[0] == 0:
        continue
    res += (data[0] * pow(data[1])) % M

print(res % M)