# 嫌いな数字
n = input()
# 病室の総数
m = input()

answer = []

for num in range(int(m)):
    # 部屋番号の入力
    r_num = input()
    # 部屋番号に嫌いな数字が含まれていない場合
    if not n in r_num:
        answer.append(r_num)

if len(answer) == 0:
    print("none")
else:
    for room in answer:
        print(room)