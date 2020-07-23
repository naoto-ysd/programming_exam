# N = int(input())
# person = {}

# # 標準入力で与えられた値の数だけ繰り返す
# for i in range(N):
#     s,a = input().split()
#     a = int(a)
#     person[s] = a


# for key in person:
#     print(key + " " + str(person[key]+1))

N = int(input())

for _ in range(N):
    s_a = input().split()
    print(s_a[0], int(s_a[1]) + 1)