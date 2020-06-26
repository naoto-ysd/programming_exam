num_list = []
for _ in range(6):
    num_list.append(int(input()))

sorted_numlist = sorted(num_list)
uniq_sorted_numlist = set(sorted_numlist)

for num in uniq_sorted_numlist:
    # 要素を出力
    print(num)