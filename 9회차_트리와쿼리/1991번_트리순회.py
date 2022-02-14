import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque
n = int(input())

tree = {}
for i in range(n):
    a,b,c = input().split()
    tree[a] = [b,c]

def preorder(current):
    if current == '.':
        return
    print(current, end="")
    preorder(tree[current][0])
    preorder(tree[current][1])
def postorder(current):
    if current == '.':
        return
    postorder(tree[current][0])
    postorder(tree[current][1])
    print(current, end="")


def inorder(current):
    if current == '.':
        return

    inorder(tree[current][0])
    print(current, end="")
    inorder(tree[current][1])

preorder("A")
print()
inorder("A")
print()
postorder("A")