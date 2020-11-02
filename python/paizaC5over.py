n = int(input())

num = 0

for n in range(n):

  # 数値の入力
  input_num = int(input())

  # 5以上だったら
  if input_num >= 5:
    num = num + input_num

print(num)