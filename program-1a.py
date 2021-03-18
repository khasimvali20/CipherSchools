for i in range(5):
    for j in range(5,0,-1):
        if i+1 >= j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")