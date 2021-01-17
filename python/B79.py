s, t = input().split(" ")
namelist = list(s + t)

result = []

for num in range(0, 2):
    value = []

    if num == 0:
        namelist = list(s + t)
    else:
        namelist = list(t + s)

    for i in range(0, len(namelist)):
        value.append(ord(namelist[i]) - 96)

    for i in range(0, len(value)):

        for j in range(0, len(value) - 1):
            value[j] = value[j] + value[j + 1]
            
            if(value[j] > 101):
                value[j] -= 101

        if(len(value) >= 2):
            # value配列の末尾を削除
            del value[len(value) - 1]

    result.append(value[0])


if(result[0] > result[1]):
    print(result[0])
else:
    print(result[1])