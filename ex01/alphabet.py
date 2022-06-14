import random
import datetime

global ln, mn,g,max_n
ln=8
mn=2
g=True
max_n=10
def alphabet_game():
    global g
    a=[]
    for i in range(65,91):
        a.append(chr(i))
    t=random.sample(a,ln)
    h=random.sample(t,len(t)-mn)
    print("対象文字:")
    for i in t:
        print(i,end=" ")
    print("表示文字:")
    for i in h:
        print(i,end=" ")
    n=input("欠損文字はいくつあるでしょうか？")
    if int(n)==mn:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        for i in range(len(mn)):
            a=input(f"{i+1}つ目の文字を入力してください:")
            if a in h:
                h.remove(a)
            else:
                print("不正解です。またチャレンジしてください")
                g=False
                return 

    else:
        print("不正解です。またチャレンジしてください")
        g=False
        return





if __name__ =="__main__":
    st=datetime.datetime.now()
    a=0
    t=0
    while a==0:
        alphabet_game()
        if g==True:
            ed=datetime.datetime.now()
            print("ゲームクリアです")
            print((ed-st).second)
            a=1
        else:
            if t<=max_n:
                t+=1
