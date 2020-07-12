d = []

for i in range(5):
  d.append(int(input()))

for num in range(len(d)-1):
  print(d[num+1] - d[num])