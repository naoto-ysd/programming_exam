# 入力値を変数に格納
button, rule = input().split()
count = int(input())

# button変数は数値にしておく
button = int(button)
rule = int(rule)

# 入力値を配列に格納
kaitou = []
kaitou = input().split()

# 配列の初期化　この配列に模範解答を代入する
mohan = []

# 模範解答を用意する
for w in range(count):
    if (w + 1) > button:
        mohan.append((w + 1) - button)
    else:
        mohan.append(w + 1)

# 変数の初期化
score = 0
miss = 0

# 模範回答と実際の回答ログを付き合わせる
for i in range(count):
    if int(kaitou[i]) == mohan[i]:
        score += 1000
    else:
        miss += 1

if miss >= rule:
    print(-1)
else:
    print(score)