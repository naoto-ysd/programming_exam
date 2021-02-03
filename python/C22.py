# 日数
n = int(input())

answer = []
answer_tmp = []

# 高値を一時的に代入しておく変数
h_tmp = 0
# 安値を一時的に代入しておく変数
l_tmp = 0

# s_i は始値、e_i は終値、h_i は高値、l_i は安値を表す
for i in range(n):
    # s_i,e_i,h_i,l_i = (int(x) for x in input().split())
    answer_tmp = list(map(int,input().split(" ")))

    # ループの最初だけ行う処理。配列の初期化。
    if i == 0:
        answer = answer_tmp
    elif i == n - 1:
        answer[1] = answer_tmp[1]

    # 高値を配列に格納
    if answer[2] < answer_tmp[2]:
        answer[2] = answer_tmp[2]

    # 安値を配列に格納
    if answer[3] > answer_tmp[3]:
        answer[3] = answer_tmp[3]

print(*answer)