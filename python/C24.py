num = int(input())
answer1 = 0
answer2 = 0

for n in range(num):
    tmp = input()

    if tmp[0:3] == "SET":
        order = tmp.split(" ")

        if order[1] == "1":
            answer1 = int(order[2])
        else:
            answer2 = int(order[2])
        
    elif tmp[0:3] == "ADD":
        order = tmp.split(" ")
        answer2 = answer1 + int(order[1])

    else:
        order = tmp.split(" ")
        answer2 = answer1 - int(order[1])

print(str(answer1) + " " + str(answer2))
