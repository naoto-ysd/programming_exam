# 高さH 横幅W 変更後の横幅X
H, W, X = (int(x) for x in input().split())
s = ""
answer = []

for num in range(H):
    # 入力された文字列を配列に代入
    s += input()

for i in range(0,len(s),X):
    print(s[i:i+X])