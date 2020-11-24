import random                              #隨機排序
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(number)
lucky=''
a=0   #使A、B的數量都先為0
b=0
for i in range(4):
    lucky+=str(number[i])
while(True):
    guessnumber=input('請輸入4個不同的數字: ')
    if not guessnumber.isdigit():   #判斷輸入是否為4位數字
        pass
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
