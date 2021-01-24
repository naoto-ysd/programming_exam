N = int(input())
G = input()
S_x = []
count = 0

for n in range(N):
    S_x.append(input())

for log in S_x:
    if G in log:
        print(log)
        count += 1

if count == 0:
    print("None")