import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**5)
n,p,q = map(int,input().split())

dic = dict()
dic[0] = 1
def solve(n):
   if n in dic:
       return dic[n]
   else:
       dic[n] = solve(n//p) + solve(n//q)
       return dic[n]

print(solve(n))