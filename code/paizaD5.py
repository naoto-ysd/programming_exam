m,n = input().split()
m = int(m)
n=int(n)
num = str(m)

for i in range(9):
    m += n
    num+=" " + str(m)

print(num)