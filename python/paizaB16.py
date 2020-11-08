w, h, n = input().split()
w = int(w)
h = int(h)
n = int(n)

x, y = input().split()
x = int(x)
y = int(y)

for i in range(n):
    sabun = 0
    muki, kyori = input().split()

    kyori = int(kyori)

    if muki == 'U':
        sabun = y + kyori
        if sabun >= h:
            amari = sabun % h

        y = amari

    elif muki == 'D':
        sabun = y - kyori
        if sabun < 0:
            amari = sabun % h

        y = amari

    elif muki == "L":
        sabun = x - kyori
        if sabun < 0:
            amari = sabun % w

        x = amari


    elif muki == "R":
        sabun = x + kyori
        if sabun >= w:
            amari = sabun % w

        x = amari

print(str(x) + " " + str(y))