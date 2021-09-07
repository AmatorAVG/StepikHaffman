import logging as log
log.basicConfig(level=log.INFO)

import sys
input = sys.stdin
input = open('1.txt', 'r')

n, *A = map(int, input.readline().split())
k, *B = map(int, input.readline().split())

S = {A[x]: x+1 for x in range(n)}
log.debug(S)
log.debug(S.get(23, -1))

log.debug(f'{n} {A}')
log.debug(f'{k} {B}')

for i in range(k):
    # try:
    #     index = A.index(B[i])+1
    # except ValueError:
    #     index = -1
    index = S.get(B[i], -1)
    log.debug(f'{B[i]}: {index}')
    print(index, end=' ')