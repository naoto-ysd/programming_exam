n,s = input().split()
n = int(n)

if s == "km":
    print(n*1000*100*10)
elif s == "m":
    print(n*100*10)
elif s == "cm":
    print(n*10)