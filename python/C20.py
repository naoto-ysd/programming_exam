m,p,q = input().split()

m = int(m)
p = int(p)/100
q = int(q)/100

# 生鮮食品の売れ残り
M = m - (m * p)

# お惣菜の売れ残り
Q = M - (M * q)

print(Q)