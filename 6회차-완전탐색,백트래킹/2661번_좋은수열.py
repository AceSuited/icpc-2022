import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())


candidate = []

def check(seq):
    for length in range(1, len(seq) // 2 + 1):
        for start in range(len(seq) - length * 2 + 1):
            if seq[start:start+length] == seq[start+length:start + length+length]:
                return False
    return True

def solve(depth, picked):
    global candidate
    if not check(picked):
        return

    if depth == n:
        print("".join(map(str,picked)))
        sys.exit()
    else:
        for i in range(3):
            picked.append(i+1)
            solve(depth + 1, picked)
            picked.pop()

solve(0,[])