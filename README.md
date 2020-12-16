# xAxB人猜
```
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
```
# xAxB 電腦猜
```
import itertools as it
import random
lst=[i for i in range(10)]
poss=list(it.permutations(lst,4))             #電腦把所有組合都列出
random.shuffle(poss)
q=int(input("請輸入電腦猜的號碼:"))                 #電腦猜的號碼
comguess=0                                         #電腦猜的次數
while True:
    comguess +=1                                   #每猜一次加一
    possanswer=[]                                  #可能的正確答案
    print(f"\n電腦第{comguess}次猜:{''.join([str(i)for i in poss[0]])}")
    ABnumber=input("AB狀況:")                   #人進行判斷
    A=int(ABnumber[0])                          #提取A、B數量
    B=int(ABnumber[2])
    if A ==4:
        print("電腦答對")
        break
    for i in range(len(poss)):
        count_a=0
        count_b=0
        for j in range(len(poss[0])):
            if poss[i][j] in poss[0]:
                if j==poss[0].index(poss[i][j]):
                    count_a+=1
                else:
                    count_b+=1
        if count_a==A and count_b==B:                #把可能的正確答案放進去
            possanswer.append(poss[i])
    poss=possanswer                              #可能的正確答案取代之前的所有
 ```
