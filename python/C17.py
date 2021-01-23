a, b = input().split()
a = int(a)
b = int(b)
n = int(input())
A = []
B = []

for num in range(n):
    Input_A, Input_B = input().split()
    A.append(int(Input_A))
    B.append(int(Input_B))

for i in range(n):
    if A[i] > a:
        print("Low")
    elif A[i] == a:
        if B[i] < b:
            print("Low")
        else:
            print("High")
    else:
        print("High")