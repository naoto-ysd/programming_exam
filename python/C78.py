N, c_1, c_2 = (int(x) for x in input().split())
answer = 0

# 購入した株の数
count = 0

for day in range(N):
    
    # その日の株価を入力
    c_day = int(input())

    # 最終日の場合
    if day == (N-1):
        # 株を持っていたら
        if count > 0:
            answer += c_day * count

    else:
        # 買いのパターン
        if c_day <= c_1:
            answer -= c_day
            count += 1
        # 売りのパターン
        elif c_day >= c_2:
            answer += c_day * count
            count = 0

print(answer)