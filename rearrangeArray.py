def arrange(A):
    B = A.copy()
    for i in range(len(A)):
        A[i] = B[A[i]]

a = [4, 0, 2, 1, 3]
arrange(a)
for i in a:
    print(i)