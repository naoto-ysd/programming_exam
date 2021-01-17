keybord = input()
taikyu = keybord.split()
taikyu = [int(t) for t in taikyu]

S = input()


alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

answer = ""

for n in S:
  if taikyu[alfa.index(n)] >= 1:
    answer = answer + n
  
  taikyu[alfa.index(n)] = taikyu[alfa.index(n)]-1

print(answer)
