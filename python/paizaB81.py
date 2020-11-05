H,W = input().split()

kadan = []
himo = 0

for n in range(int(H)):
    kadan.append(input())

# 配列の繰り返し処理
for i in range(int(H)):
    # 文字列に＃が含まれていた場合
    if kadan[i].find("#") >= 0:
