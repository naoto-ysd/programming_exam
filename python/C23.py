WinNum = input().split(" ")
N = int(input())
kuji = [ list(input().split(" ")) for x in range(N) ]
answer = []

for kujinum in range(N):
    counter = 0
    for i in kuji[kujinum]:
        counter += WinNum.count(i)

    answer.append(counter)

# 一致数の出力
for j in answer:
    print(j)