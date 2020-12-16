import random                              #隨機排序
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(number)
lucky=''
a=0   #使A、B的數量都先為0
b=0
for i in range(4):
    lucky+=str(number[i])
while(True):
    guessnumber=input("請輸入4個不同的數字: ")
    if len(guessnumber)!=len(lucky):
        print("號碼個數要有4位")
        continue
    p=0
    for i in range(len(guessnumber)):                 #檢測是否輸入重複的號碼
        for j in range(i):
            if guessnumber[j]==guessnumber[i]:
                print("請勿輸入重複號碼")
                p=1
                break
        if p==1:
            break
    else:
        if guessnumber==lucky:
            print('恭喜你答對')
            break
        for i in range(4):                               #比較兩個數
            for j in range(4):
                if i==j and guessnumber[i]==lucky[j]:   #位子一樣、數字一樣
                    a+=1
                elif guessnumber[i]==lucky[j]:          #有同樣的數字
                    b+=1
        print(a,'A',b,'B')            #輸出xAxB
        a=0
        b=0
