num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    # 入力された数字をキーにして、キーに対応した文字列を設定している
    inputs[int(tmp[1])] = tmp[0]

inputs = sorted(inputs.items())

for i in inputs:
    print(i[1])