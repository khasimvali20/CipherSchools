a = int(input("Enter your budget : "))
bg = a

pn = []
q = []
p = []
print("1.Add an item")
print("2.Exit")
n=int(input("Enter your choice : "))
while True:
    if(n==1 and bg>0):
        b=input("Enter Product : ")
        c=input("Enter Quantity in kgs : ")
        d=float(input("Enter Price : "))
        if d>bg:
            print("Can't Buy the product")
        else:
            if b in pn:
                f=pn.index(b)
                q.remove(q[f])
                p.remove(p[f])
                q.insert(f,c)
                p.insert(f,d)
                bg = a - sum(p)
                print("\namount left", bg)

            else:
                pn.append(b)
                q.append(c)
                p.append(d)
                bg = a - sum(p)
                print("\namount left", bg)


        print("1.Add an item")
        print("2.Exit")
        n = int(input("Enter your choice : "))
    elif bg<= 0:
        print("NO BUDGET")
    else:
        break
print("Amount left : ", bg)
if bg in p:
    print("Amount left can buy you a ", pn[p.index(bg)])

print("GROCERY LIST IS:")
print("Product name    Quantity    Price")
for i in range(len(pn)):
    print(pn[i], q[i], p[i])