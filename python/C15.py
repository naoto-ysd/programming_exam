import math
# レシートの数
N = int(input())

# ポイント数の初期化
point = 0

# レシートの数だけ処理を繰り返す
for i in range(N):
    # 日付と購入金額の入力
    d_i,p_i = (int(x) for x in input().split())

    # ポイント3倍の日
    if "3" in str(d_i):
        point += math.floor(p_i * 0.03)
    # ポイント5倍の日
    elif "5" in str(d_i):
        point += math.floor(p_i * 0.05)
    else:
        point += math.floor(p_i * 0.01)

print(point)