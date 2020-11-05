H,W = input().split()
H = int(H)
W = int(W)

kadan = []
himo = 0

for n in range(H):
    kadan.append(input())

# 配列の繰り返し処理
for n in range(H):
    for i in range(W):
        # 文字列に＃が含まれていた場合
        if kadan[n][i] == "#":
            himo += 4

            # 処理しているのが最初の行だったら
            if n == 0:

                # 一番左の列だったら
                if i == 0:
                  # 下のマスの確認
                  if kadan[n+1][i] == "#":
                      himo =  himo -1
                  # 右のマスの確認
                  if kadan[n][i+1] == "#":
                      himo =  himo -1

                # 一番右の列だったら
                elif i == W -1:
                    # 下のマスの確認
                    if kadan[n+1][i] == "#":
                        himo =  himo -1
                    # 左のマスの確認
                    if kadan[n][i-1] == "#":
                        himo =  himo -1
                
                else:
                    if kadan[n+1][i] == "#":
                        himo =  himo -1
                    # 右のマスの確認
                    if kadan[n][i+1] == "#":
                        himo =  himo -1
                    # 左のマスの確認
                    if kadan[n][i-1] == "#":
                        himo =  himo -1

            # 処理しているのが最後の行だったら
            elif n == H-1:
                # 一番左の列だったら
                if i == 0:
                    # 上のマスの確認
                    if kadan[n-1][i] == "#":
                        himo =  himo -1
                    # 右のマスの確認
                    if kadan[n][i+1] == "#":
                        himo =  himo -1

                # 一番右の列だったら
                elif i == W -1:
                    # 上のマスの確認
                    if kadan[n-1][i] == "#":
                        himo =  himo -1
                    # 左のマスの確認
                    if kadan[n][i-1] == "#":
                        himo =  himo -1
                
                else:
                    # 上のマスの確認
                    if kadan[n-1][i] == "#":
                        himo =  himo -1
                    # 左のマスの確認
                    if kadan[n][i-1] == "#":
                        himo =  himo -1
                    # 右のマスの確認
                    if kadan[n][i+1] == "#":
                        himo =  himo -1

            else:
                # 一番左の列だったら
                if i == 0:
                    # 上のマスの確認
                    if kadan[n-1][i] == "#":
                        himo =  himo -1
                    # 下のマスの確認
                    if kadan[n+1][i] == "#":
                        himo =  himo -1
                    # 右のマスの確認
                    if kadan[n][i+1] == "#":
                        himo =  himo -1

                # 一番右の列だったら
                elif i == W -1:
                    # 上のマスの確認
                    if kadan[n-1][i] == "#":
                        himo =  himo -1
                    # 下のマスの確認
                    if kadan[n+1][i] == "#":
                        himo =  himo -1
                    # 左のマスの確認
                    if kadan[n][i-1] == "#":
                        himo =  himo -1

                else:
                    # 上のマスの確認
                    if kadan[n-1][i] == "#":
                        himo =  himo -1
                    # 下のマスの確認
                    if kadan[n+1][i] == "#":
                        himo =  himo -1
                    # 右のマスの確認
                    if kadan[n][i+1] == "#":
                        himo =  himo -1
                    # 左のマスの確認
                    if kadan[n][i-1] == "#":
                        himo =  himo -1

print(himo)