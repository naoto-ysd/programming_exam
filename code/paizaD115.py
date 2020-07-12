import math
N=int(input())

if N%2 == 1:
    N = N-1
    print(math.floor(N/2))
else:
    print(math.floor(N/2))