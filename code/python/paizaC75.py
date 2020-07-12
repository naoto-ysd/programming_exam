import math

N,M = input().split()

# N はじめにチャージされている金額
N = int(N)
# M バスの乗車回数
M = int(M)
# 運賃を格納する配列
f = []
# カードの残高
c = N
# ポイントの初期化
p = 0

# バスの乗車回数の分だけ、料金を配列に格納する
for i in range(M):
    f.append(int(input()))

for num in f:
    if p >= num:
        p -= num 
    else:
        c -= num
        p += num/10
    print(str(c) + ' ' + str(math.floor(p)))