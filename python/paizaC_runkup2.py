time = int(input())
result = 0

for i in range(time):
    std_in = input()
    array = std_in.split()

    if array[0] == array[1]:
        result += int(array[0]) * int(array[1])
    else:
        result += int(array[0]) + int(array[1])

print(result)