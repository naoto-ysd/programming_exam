ATK, DEF, AGI = (int(x) for x in input().split())

# 進化先のモンスター数
N = int(input())

# 進化可能なモンスターを格納しておく配列
answer = []

# 進化先のモンスターの名前と進化条件を入力
for num in range(N):
    # 初期化
    s_num, MINATK_num, MAXATK_num, MINDEF_num, MAXDEF_num, MINAGI_num, MAXAGI_num = input().split()
    if ATK >= int(MINATK_num) and ATK <= int(MAXATK_num) and DEF >= int(MINDEF_num) and DEF <= int(MAXDEF_num) and AGI >= int(MINAGI_num) and AGI <= int(MAXAGI_num):
        answer.append(s_num)

if len(answer) == 0:
    print("no evolution")
else:
    for monster in answer:
        print(monster)