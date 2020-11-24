import random                              #隨機排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
answer=''
a_count=0   #使A、B的數量都先為0
b_count=0
for i in range(4):
    answer+=str(items[i])

while(True):
    guessnumber=input('請輸入4個不同的數字: ')
    if not guessnumber.isdigit():   #判斷輸入是否為4位數字
        pass
    elif guessnumber
    else:
        if guessnumber==answer:
            print('恭喜你答對')
            break
        for i in range(4):
            for j in range(4):
                if i==j and guessnumber[i]==answer[j]:
                    a_count+=1
                elif guessnumber[i]==answer[j]:
                    b_count+=1
        print(a_count,'A',b_count,'B')
        a_count=0
        b_count=0