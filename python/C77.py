import math

# kは学生の人数 nはレポートの問題数
k, n = (int(x) for x in input().split())

# 1問あたりの配点
haiten = 100/n

point = []

for i in range(k):
    # i番目の学生のレポートを提出した日を表す整数d_i、i番目の学生が正解した問題数を表す整数 a_i がこの順に半角スペース区切りで与えられます。
    d_i, a_i = (int(x) for x in input().split())

    # 提出が10日以上遅れた場合
    if d_i >= 10:
        # 点数を0にする
        point.append(0)
    # 提出が1~9日遅れた場合
    elif d_i >= 1 and d_i <= 9:
        # 点数を8割にする
        point.append(math.floor((haiten * a_i) * 0.8))
    else:
        point.append(math.floor(haiten * a_i))

for n in point:
    if n >= 80:
        print("A")
    elif n >= 70:
        print("B")
    elif n >= 60:
        print("C")
    else:
        print("D")