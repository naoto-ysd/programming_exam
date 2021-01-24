xc, yc, r_1, r_2= [int(x) for x in input().split()]
n = int(input())
YesOrNo = []

def hantei(x, y):
    if r_1**2 <= (x - xc)**2 + (y - yc)**2 <= r_2**2:
        return "yes"
    else:
        return "no"

for i in range(n):
    x, y = [int(j) for j in input().split()]
    YesOrNo.append(hantei(x, y))
    
for k in YesOrNo:
    print(k)