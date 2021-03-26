# 変数、引数 小文字のみ、必要に応じて単語をアンダースコアで区切る
# 1文字変数は使わない。iとかoは1と0で間違ったりするから
# 定数	大文字のみ、単語をアンダースコアで区切る。通常、モジュールレベル（関数の外側）に書く
# 関数、メソッド 小文字のみ。必要に応じて単語をアンダースコアで区切る。
# クラス、例外 CapWords方式 (単語の先頭を大文字にする。アンダースコアは使わない 例: GetUser)

# 模範回答
N = int(input())
# 配列の要素数を決める。
kingin = [0] * N

for i in range(N):
    [a, b] = [int(j) for j in input().split()]
    # 配列の中身(金と銀)を逆にしている
    kingin[i] = [b, a]

# 配列(kingin)に対してソートをかけている。デフォルトで多次元配列の最初の要素同士で比較するっぽい。
kingin.sort(reverse=True)
# 以下でも同様のソートが可能
# kingin.sort(reverse=True, key=lambda x:(x[0], x[1]))

for i in range(N):
    [a, b] = kingin[i]
    print(b, a)