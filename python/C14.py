#箱の数n, ボールの半径r 表す整数
n,r = (int(x) for x in input().split())

answer = []

for num in range(n):
    #n個目の箱の高さ、幅、奥行きを表す整数。
    h_n, w_n, d_n = (int(x) for x in input().split())

    # 箱の高さ、幅、奥行きがボールの直径より大きいか判定
    if r * 2 <= h_n and r * 2 <= w_n and r * 2 <= d_n:
        answer.append(num+1)

for box in answer:
    print(box)