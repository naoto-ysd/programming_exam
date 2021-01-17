# s = input()

# # 入力された文字列の結合
# String = s.split(" ")

# # 回答をいれる配列
# answer = []

# # 配列の要素数で繰り返す
# for s in String:
#     if s.istitle() or s[0].isdecimal():
#         answer.append(s)

# print(len(list(set(answer))))

# inp = input().split(",")
# tmp = ""
# answer = []

# for num in range(len(inp)):
#     # 偶数番目の場合
#     if num % 2 == 1:
#         answer.append(inp[num])
    
#     # 前週で読み込んだ値と同じ場合は配列に残しておく
#     if tmp == inp[num]:
#         answer.append(tmp)

#     # 読み込んだ値を変数に入れておく
#     tmp = inp[num]

# print(*answer, sep=', ')

