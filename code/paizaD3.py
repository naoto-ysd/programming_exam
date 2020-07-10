n = int(input())
ans = ""

for i in range(9):
    if i == 8:
        ans += str(n * (i+1))
    else:
        ans += str(n * (i+1)) + " "

print(ans)