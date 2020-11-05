H,W = input().split()

kadan = []
himo = 0

for n in range(int(H)):
    kadan.append(input())

# 配列の繰り返し処理
for n in range(int(H)):
    for i in range(int(W)):
        # 文字列に＃が含まれていた場合
        if kadan[n][i] == "#":
            himo += 4
            # 上のマスの確認
            if kadan[n-1][i] == "#":
                himo =  himo -1
            # 下のマスの確認
            elif kadan[n+1][i] == "#":
                himo =  himo -1
            # 右のマスの確認
            elif kadan[n][i+1] == "#":
                himo =  himo -1
            # 左のマスの確認
            elif kadan[n][i-1] == "#":
                himo =  himo -1

print(himo)