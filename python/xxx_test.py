# 使用言語 Python3

# 保守性重視の関数
# 引数で受け取った配列と、answer1関数の中で作成した配列を比較し、線形探索を行うことで解を求める。
def answer1(arg_array):
    # 引数で受け取った配列を昇順に並び替える
    asc_array = sorted(arg_array)
    # 比較用の配列の宣言。後続の処理でasc_arrayとtmp_arrayを比較する
    tmp_array = []

    # 引数で受け取った配列の最大値を求める
    max_element = max(asc_array)

    # 比較用の配列を作成する。要素数はasc_arrayの最大値と同じにする。
    # 例:asc_arrayが[0, 1, 2, 3, 4] だった場合、tmp_arrayは[1, 2, 3, 4, 5]となる
    for num in range(max_element + 1):
        tmp_array.append(num + 1)

    # tmp_arrayの要素を一つずつ取り出しtmpに代入する。tmpの値をasc_arrayと比較する。
    for tmp in tmp_array:
        # tmpにasc_arrayが含まれるか検索する。存在しない場合はその値が「配列に含まれない最小の自然数」 となる。
        if not tmp in asc_array:
            answer = tmp 
            print("回答" + str(answer))
            break



# パフォーマンス重視の関数。二分探索を行うことで解を求める。
def answer2(arg_array):

    # 引数で受け取った配列から重複を排除
    dup_array = list(set(arg_array))
    # 引数で受け取った配列を昇順に並び替える
    tmp_asc_array = sorted(dup_array)
    # 0未満の要素は二分探索を行う際に不必要であるため削除
    asc_array = [element for element in tmp_asc_array if element > 0]

    # 探索する範囲の左端を設定
    left = 0
    # 探索する範囲の右端を設定
    right = len(asc_array) - 1

    while left <= right:
        # 探索する範囲の中央を計算
        mid = (left + right) // 2

        # 二分探索で一番左まで検索していた場合の処理
        if mid == 0:
            if asc_array[0] == 1:
                print("回答:" + str(2))
            else:
                print("回答:" + str(1))
            break

        # 中央の値と一致した場合は配列の中央から右側に配列に含まれない最小の自然数」ある。
        elif asc_array[mid] == mid + 1:
            # left == rightになるということは、配列の中を全て調べ尽くした状態となる。
            if left == right:
                # 見つからなかった場合、配列の最大値に1を足した数字を返す
                print("回答:" + str(max(asc_array)+1))
            
            # 検索する範囲の左側をmid(中央の値)に置き換えることで、検索範囲を右半分に絞り込む。
            left = mid + 1

        # 配列の値が中央の値よりも大きい場合は配列の中央から左側に「配列に含まれない最小の自然数」ある。
        elif asc_array[mid] > mid + 1:
            # 検索する範囲の右側をmid(中央の値)に置き換えることで、検索範囲を左半分に絞り込む。
            right = mid - 1

        elif asc_array[mid] != mid + 1:
            print("回答:" + str(mid))
            break


# テスト用
# answer1([0, 1, 2, 3, 4])
# answer1([1, 1, 2, 2, 3, 5, 6, 4, 4, 5])
# answer1([1, 3, 5, 6])
# answer1([73, 93, 21, -6, 1])
# answer1([3, 5, 6])

# answer2([0, 1, 2, 3, 4])
# answer2([1, 1, 2, 2, 3, 5, 6, 4, 4, 5])
# answer2([1, 3, 5, 6])
# answer2([73, 93, 21, -6, 1])
# answer2([3, 5, 6])