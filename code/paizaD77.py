a,b = input().split()
a = int(a)
b = int(b)

answer = a * b

if answer >= 10000:
    print("NG")
else:
    print(answer)