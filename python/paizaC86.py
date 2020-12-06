S = input()

answer = ""
target = ["a","i","u","e","o","A","I","U","E","O"]

for n in range(len(S)):
    if not S[n:n+1] in target:
        answer += S[n:n+1]

print(answer)