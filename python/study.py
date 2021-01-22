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