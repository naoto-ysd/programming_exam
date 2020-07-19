Q = int(input())

ary = []
yakusu = []
num = 0

for i in range(Q):
    ary.append(int(input()))


for w in range(len(ary)):
    count = ary[w]

    # 第2引数以降の数だけ繰り返す
    for s in range(count-1):

        if ary[w]%(s+1) == 0:
            yakusu.append(s+1)
    s = 0

    for n in yakusu:
        num += n

    yakusu = []

    if num == ary[w]:
        print("perfect")

    elif abs(num-ary[w]) == 1:
        print("nearly")
    
    else:
        print("neither")
    
    num = 0