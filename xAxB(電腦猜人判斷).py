import itertools as it
import random
lst=[i for i in range(10)]
possible=list(it.permutations(lst,4))             #電腦把所有組合都列出
random.shuffle(possible)
q=int(input("請輸入電腦猜的號碼:"))                 #電腦猜的號碼
comguess=0                                         #電腦猜的次數
while True:
    comguess +=1                                   #每猜一次加一
    possanswer=[]                                  #可能的正確答案
    print(f"\n電腦第{comguess}次猜:{''.join([str(i)for i in possible[0]])}")
    ABnumber=input("AB狀況:")                   #人進行判斷
    A=int(ABnumber[0])                          #提取A、B數量
    B=int(ABnumber[2])
    if A ==4:
        print("電腦答對")
        break
    for i in range(len(possible)):
        count_a=0
        count_b=0
        for j in range(len(possible[0])):
            if possible[i][j] in possible[0]:
                if j==possible[0].index(possible[i][j]):
                    count_a+=1
                else:
                    count_b+=1
        if count_a==A and count_b==B:                #把可能的正確答案放進去
            possanswer.append(possible[i])
    possible=possanswer                              #可能的正確答案取代之前的所有
