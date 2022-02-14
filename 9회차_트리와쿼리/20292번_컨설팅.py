import sys
input = lambda:sys.stdin.readline().strip()

instructions = []
while True:
    ins = input()
    if ins == "EXIT":
        break
    else:
        instructions.append(ins.split())

buf_write = dict()
buf_read = []
if len(instructions) == 0:
    print("EXIT")
    sys.exit()


if len(instructions[0]) == 2:
    buf_read.append(instructions[0][1])
else:
    buf_read.append(instructions[0][1])
    buf_write[instructions[0][3]] = instructions[0][1]
print(*instructions[0])

for i in range(1, len(instructions)):
    current = instructions[i]

    if len(current) == 2:
        arg = current[1]
        if arg in buf_write:
            print("WAIT")
            buf_write.clear()
            buf_read.clear()
        buf_read.append(arg)
    else:
        arg_read = current[1]
        arg_write = current[3]
        if arg_read in buf_write:
            print("WAIT")
            buf_write.clear()
            buf_read.clear()

        if arg_write in buf_write:
            print("WAIT")
            buf_write.clear()
            buf_read.clear()

        if arg_write in buf_read and arg_read in buf_write and buf_write[arg_read] == arg_write:
            print("WAIT")
            buf_write.clear()
            buf_read.clear()

        if arg_write in buf_read:
            print("WAIT")
            buf_write.clear()
            buf_read.clear()

        buf_read.append(arg_read)
        buf_write[arg_write] = arg_read


    print(*current)

print("EXIT")