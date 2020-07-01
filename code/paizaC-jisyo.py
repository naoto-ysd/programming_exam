# 問題内容
# n 人の人に関して、それぞれの人の名前と財産が与えられます。
# その後に人名 S が与えられるので （S は最初に与えられた名前のうちのいずれか） 、 S の財産を表す整数を出力してください
# 入力は以下のフォーマットで与えられます。

# n
# s_1 a_1
# ...
# s_n a_n
# S

# 1 行目には正整数nが与えられ、 2 行目から (n + 1) 行目には、人々の名前と財産が 
# “s_i a_i” というフォーマット （s_i は人の名前を表す文字列、 a_i はその人の財産を表す整数、半角スペース区切り）
# で与えられます。 (n + 2) 行目には人名 S が与えられます (S は 2 行目から (n + 1) 行目にかけて与えられた人名のいずれか）。


# 期待する出力
# S の財産を出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。


# 空の配列を作成
# info = []

# 人数を入力
# num = input()

# 人の名前と財産を入力
# for w in range(num):
#     name, money = input().split()
#     info[]

# for i, info in enumerate(input().split()):
  

# 回答

# 人数を入力する
n = int(input())
# 財産を格納する辞書を作成
zaisan = {}

# 人数文だけ繰り返してユーザーに入力させる
for i in range(n):
    [s, a] = input().split()
    zaisan[s] = a

S = input()

print(zaisan[S])