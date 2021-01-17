num, goukaku = input().split(" ")
num = int(num)
goukaku = int(goukaku)
students = []

for i in range(num):
    score, kesseki = input().split(" ")
    score = int(score)
    kesseki = int(kesseki)

    score = score - (kesseki * 5) 

    if score < 0:
        score = 0

    if score >= goukaku:
        students.append(i+1)

for n in students:
    print(n)
