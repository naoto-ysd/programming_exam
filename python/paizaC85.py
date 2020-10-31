S = input()
len = len(S)

for n in range(3):
  plus = ""

  i = 1
  while i <= len+2:
    if n == 1:
      plus = "+" + S + "+" 
    else:
      plus = plus + "+"
    
    i += 1

  print(plus)