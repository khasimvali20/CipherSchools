alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k = 0
for i in range(5):
    for j in range(5):
        if i >= j:
            print(alpha[k], end=" ")
            k = k+1
    print(" ")