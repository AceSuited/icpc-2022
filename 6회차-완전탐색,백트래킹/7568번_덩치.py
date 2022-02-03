import sys
input = lambda:sys.stdin.readline().strip()


n = int(input())
people = []

for _ in range(n):
    people.append(list(map(int,input().split())))

def compare(person_a, person_b):
    if person_a[0] < person_b[0] and person_a[1] < person_b[1]:
        return True
    else:
        return False
result = []
for i in range(n):
    current = people[i]
    cnt = 0
    for j in range(n):
        if compare(current, people[j]):
            cnt += 1

    result.append(cnt + 1)

print(*result)
