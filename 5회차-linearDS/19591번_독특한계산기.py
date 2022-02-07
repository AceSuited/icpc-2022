import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()
import re


priority = {"*" : 0 , "/" : 0, "+" : 1, "-" : 1}
eq = input()


operator =re.split('[0-9]',eq)
operands = re.split('\+|\-|\*|/', eq)

deq_operator = deque([])
deq_operand = deque([])
for elem in operator:
    if elem == '':
        continue
    else:
        deq_operator.append(elem)
for elem in operands:
    if elem == '':
        continue
    else:
        deq_operand.append(int(elem))

if eq[0] == "-":
    deq_operand[0] = -deq_operand[0]
    deq_operator.popleft()


def calcualate(a, b, operator):

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:
        if a < 0 or b < 0:
            return - (abs(a) // abs(b))

        return a // b


while deq_operator:
    front, end = deq_operator[0], deq_operator[-1]
    if len(deq_operator) == 1:
        deq_operand.append(calcualate(deq_operand.popleft(), deq_operand.popleft(), deq_operator.pop()))
        continue

    if priority[front] > priority[end]:
        operator = deq_operator.pop()
        a, b = deq_operand.pop(), deq_operand.pop()
        deq_operand.append(calcualate(b, a, operator))

    elif priority[front] < priority[end]:
        operator = deq_operator.popleft()
        a, b = deq_operand.popleft(), deq_operand.popleft()
        deq_operand.appendleft(calcualate(a, b, operator))

    else:

        a_end, b_end = deq_operand[-2], deq_operand[-1]
        operator_end = deq_operator[-1]
        cal_end = calcualate(a_end, b_end, operator_end)

        a_front, b_front = deq_operand[0], deq_operand[1]
        operator_front = deq_operator[0]
        cal_front = calcualate(a_front, b_front, operator_front)

        if cal_end > cal_front:
            deq_operator.pop()
            deq_operand.pop()
            deq_operand.pop()
            deq_operand.append(cal_end)
        else:
            deq_operator.popleft()
            deq_operand.popleft()
            deq_operand.popleft()
            deq_operand.appendleft(cal_front)

print(deq_operand.pop())