E = input().split("+")

answer = 0

for num in range(len(E)):
    answer += E[num].count("<") * 10
    answer += E[num].count("/")

print(answer)