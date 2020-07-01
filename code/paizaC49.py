N = int(input())

# 移動ログは配列にいれる
log = []

# 現在位置を示す変数
current = 1

for i in range(N):
    log.append(int(input()))

move = 0


for w in range(len(log)):
    move = move + abs(current - log[w])
    current = log[w]

print(move)