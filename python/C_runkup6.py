num = int(input())

for i in range(num):
    i += 1
    if i%3 == 0:
        if i%5 == 0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
# inputs = {}

# for i in range(num):
#     tmp = input().split()
#     # 入力された数字をキーにして、キーに対応した文字列を設定している
#     inputs[int(tmp[1])] = tmp[0]

# inputs = sorted(inputs.items())

# for i in inputs:
#     print(i[1])