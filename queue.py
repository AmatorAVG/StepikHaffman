import heapq
input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys
# input = sys.stdin //расскомментировать при сдаче задачи в системе

n = int(input.readline())
d_sort = []

for i in range(1, n+1):
    x = input.readline().strip()
    # print(x)
    if x.startswith('Insert'):
        num = int(x.split()[1])
        # print(num)
        heapq.heappush(d_sort, -num)
        # heapq._heapify_max(d_sort)
    elif x.startswith('ExtractMax'):
        print(-heapq.heappop(d_sort))
