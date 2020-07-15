import math
import sys

# コマンドライン引数を受け取り、変数に代入
args = sys.argv
month = int(args[2])

C = int(args[1])/100
Y = int(args[1])%100

# 変数の初期化
before_space = ""
after_space = "   "
output = ""
line = ""

# 各月の日数を配列で宣言
mday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# ツェラーの公式で月初(1日)の曜日を求める
F = 1 + (26*(month+1)/10) + int(Y) + (int(Y)/4) + 5*C + (C/4)
day = int((F % 7) + 1)

# 月初(1日)の曜日を代入　月曜日だったら2,火曜日だったら3,といった具合。
start = math.floor(day)
print("Sun|Mon|Tue|Wed|Thu|Fri|Sat")

# 空白を作る。金曜日だったら6*3 = 18　となり、18個の空白を表示後に1が表示される
for i in range(start):
    before_space += "   "

for num in range(mday[month-1]):
    if day <= 7:
        # 1日目はスペースと一緒に出力する
        if num == 0:
            line += before_space + str(num +1) + after_space
        else:
            line += str(num +1) + after_space
        day += 1
    # 日曜日から月曜日まで出力する
    else:
        print(line)
        # day(曜日)の初期化
        day = 1
        line = str(num + 1) + after_space

# 最後の行を出力
print(line)

