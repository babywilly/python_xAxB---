import random
x=random.sample('1234567890',4)
while (True):
    number=input("輸入4個不同數字:")
    z = list(number)
    a=0
    for i in range(4):
        if(x[i]==z[i]):
            a=a+1
    b=0
    j=0
    while j < 4:
        k=0
        while k < 4:
            if j==k :
                k=k+1
                continue
            if(x[j]==z[k]):
                b=b+1
            k=k+1
        j=j+1
    print(a,"A", b, "B")
    if a == 4:
        print("恭喜答對")
        break