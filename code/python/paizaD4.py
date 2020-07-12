n = int(input())
ary = []
num = 0
str = ""
for i in range(n):
    ary.append(input())

for w in range(len(ary)):
    if w+1 == len(ary):
        str += ary[w] + "."
    else:
        str += ary[w] + ","


print("Hello" + " " + str)