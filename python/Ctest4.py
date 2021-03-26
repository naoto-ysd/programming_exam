# 変数、引数 小文字のみ、必要に応じて単語をアンダースコアで区切る
# 1文字変数は使わない。iとかoは1と0で間違ったりするから
# 定数	大文字のみ、単語をアンダースコアで区切る。通常、モジュールレベル（関数の外側）に書く
# 関数、メソッド 小文字のみ。必要に応じて単語をアンダースコアで区切る。
# クラス、例外 CapWords方式 (単語の先頭を大文字にする。アンダースコアは使わない 例: GetUser)


# 問題URL
# https://paiza.jp/works/mondai/c_rank_level_up_problems/c_rank_dictionary_boss/edit?language_uid=python3

# 模範回答
[p, q, r] = [int(i) for i in input().split()]
AB = {}
BC = {}

# 2 行目から (p + 1) 行目までは A グループの人の番号とその人が仕事を頼む 
# B グループの人の番号 i_a, j_a （1 ≤ a ≤ p） が半角スペース区切りで、 
# (p + 2) 行目から (p + q + 2) 行目までは B グループの人の番号とその人が仕事を頼む 
# C グループの人の番号 j’_b , k_b （1 ≤ b ≤ q） が半角スペース区切りで与えられます。

# 変数名を「_」にすることによって、「その変数を使っていません」ということを表現しています（Pythonの習慣です）。
for _ in range(p):
    [i, j] = [int(n) for n in input().split()]
    # 「1 3」と入力した場合、Aグループの1番の人がBグループの3番の人に仕事を頼む
    AB[i] = j

for _ in range(q):
    [j, k] = [int(n) for n in input().split()]
    # 「2 3」と入力した場合、Bグループの2番の人がCグループの3番の人に仕事を頼む
    BC[j] = k

AC = {}

# range(start, stop)のように引数に整数を2つ指定すると、start ≦ i < stopの連番が生成される。
# 引数startの値は結果に含まれるが引数stopの値は含まれないので注意。
for i in range(1, p + 1):
    AC[i] = BC[AB[i]]

for i, k in AC.items():
    print(i, k)


print(AB)
print(BC)