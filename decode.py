input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys
# input = sys.stdin //расскомментировать при сдаче задачи в системе
code_table = {}
n, col = map(int, input.readline().split())

res = ''

for i in range(1, n+1):
    x, y = input.readline().split()
    code_table[y] = x[:-1]

code_string = input.readline().strip()
i = 1
while len(code_string):
    cur = code_string[0:i]
    if cur in code_table:
        res += code_table[cur]
        code_string = code_string[i:]
        i = 1
    else:
        i += 1
print(res)
