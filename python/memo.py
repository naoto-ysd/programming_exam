# 標準入力から半角スペース区切りで変数に代入
m,p,q = input().split()



S = input()
for n in range(len(S)):
    # 文字列オブジェクト[開始インデックス:終了インデックス]
    # 開始インデックスと終了インデックスをコロン(:)でつなげて指定すると文字列を切り出せる
    # https://qiita.com/Kenta-Han/items/e64035e9c3e4ef08e394
    print(S[n:n+1])
    # print(S[n:n+1] in target)



E = input().split("+")
answer = 0
for num in range(len(E)):
    answer += E[num].count("<")
# 文字列中に含まれる特定の文字列の出現回数を数える
answer += E[num].count("/")


# 複数の変数を数値で入力したい場合
# input().split()で取得したstr型リストの要素「x」を順番にint型にキャストしています。
# ※変数の数を指定するので、入力される数値の数は事前に決まっていなければならない。
# https://qiita.com/daihukuchan/items/c7c807c2e01e49657e5d
a,b = (int(x) for x in input().split())
print(a+b)


# mapの使い方
# https://qiita.com/daihukuchan/items/c7c807c2e01e49657e5d
# map関数は引数に map(処理内容,繰り返し処理ができるもの)　という引数を取る
# 下記の処理では半角スペース区切りで入力した値をstr型からint型に変換している
c = map(int,input().split(" "))
print(list(c))


# 配列に数値を代入
# https://qiita.com/daihukuchan/items/c7c807c2e01e49657e5d
# map関数は引数に map(処理内容,繰り返し処理ができるもの)　という引数を取る
# 下記の処理では入力を半角スペースで区切→int型に変換→cという配列を作っている
c = list(map(int,input().split(" ")))
print(c)


# 多重配列で格納
# https://qiita.com/daihukuchan/items/c7c807c2e01e49657e5d
# map関数は引数に map(処理内容,繰り返し処理ができるもの)　という引数を取る
# 下記の処理では入力を半角スペースで区切→int型に変換→dという配列を作り、for文で繰り返して多重配列を作っている
N = 3
d = [ list(map(int,input().split(" "))) for x in range(N)]
print(d)


# for文で配列の要素を取得する
S_x = ["aa","vv","dd","ff","ww"]

for log in S_x:
    print(log)