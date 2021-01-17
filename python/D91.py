p = []
p = input().split()
count = 0

for i in range(len(p)):
    if int(p[i]) <= 2:
        count += 1

print(count)