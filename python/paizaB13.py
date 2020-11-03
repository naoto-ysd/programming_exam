import datetime
import math

a,b,c = input().split()

# 家から駅までの時間
housetostation = int(a)


# 電車に乗っている時間と駅から会社まで時間の合計
sumtime = + int(b) + int(c)

# 分を求める
trainminute = sumtime % 60
# 時間を求める
trainhour = math.floor(sumtime / 60)


# 通気時間を日付型にする
sumtime = datetime.datetime(2019, 10, 10, trainhour, trainminute, 00)


#配座駅から出る電車の本数を表す整数 N
N = int(input())

# 電車の発車時刻を格納する配列
Traintime = []

# 電車の発車時刻を入力
for n in range(N):
  hour,minute = input().split()
  dt = datetime.datetime(2019, 10, 10, int(hour), int(minute), 00)

  # 分を0埋め
  # minute = minute.zfill(2)

  # 発車時刻を配列に追加
  Traintime.append(dt)

# 出社時間
syussya = datetime.datetime(2019, 10, 10, 8, 59, 00)
# 出社時間に間に合ったデータを格納する配列
arrive = []

# 電車の
for n in range(N):
  if Traintime[n] + datetime.timedelta(hours = trainhour, minutes = trainminute) <= syussya:
    # この電車に乗ればいい。
    arrive.append(Traintime[n])

# 出社時間に間に合う電車から一番大きいものを抜き出す
# 抜き出したものから、家から駅までの時間を引く
d = max(arrive) - datetime.timedelta(minutes = housetostation)
print(d.strftime('%H:%M'))