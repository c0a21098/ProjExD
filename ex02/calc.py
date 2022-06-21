import tkinter as tk
import tkinter.messagebox as tkm
import math


def button_click(event):
    btn = event.widget
    num = btn["text"]  #クリックされたボタンの文字をnumとする

    if num == "=":
        eqn = entry.get()   #entryに入力された文字をeqnとして取得する
        ans = eval(eqn)    #eqnを計算する
        entry.delete(0,tk.END)  #entryの文字を消去する
        entry.insert(tk.END,ans)  #entryに計算した値を入力する

    elif num == "AC":
        entry.delete(0,tk.END)   #entryの文字を消去する

    elif num == "税込":
        eqn = entry.get()
        tax = math.floor(eval(eqn)*1.1)  #取得した値に１．１をかけて小数点以下を切り捨てる
        entry.delete(0,tk.END)
        entry.insert(tk.END,tax)

    #tkm.showinfo("",f"{num}のボタンがクリックされました")
    else:
        entry.insert(tk.END,num)


if __name__ == "__main__":
    root = tk.Tk()  #ウィンドウの作成
    root.title("超高機能電卓")  #タイトルを超高機能電卓とする
    #root.geometry("300x500")

    entry = tk.Entry(root,         #入力された数字や計算結果が表示されるentryの作成
                    justify="right",
                    width=10,
                    font=("Times New Roman",40)
                    )
    entry.grid(row=0,column=0,columnspan=4)

    r,c=1,0      #ｒ：行番号　ｃ：列番号
    for i,num in enumerate([9,8,7,"AC",6,5,4,"税込",3,2,1,"+","",0,"","="]):
        btn = tk.Button(root,    #各ボタンの作成
                    text = f"{num}",
                    width=4,
                    height=2,
                    font = ("Times New Roman",30)
                    )
        btn.bind("<1>",button_click)   #ボタンをクリックした場合にbutton_click関数を実行する
        btn.grid(row=r,column=c)
        c+=1
        if (i+1)%4 == 0:   #４列になるようにする
            r+=1
            c=0
            
    root.mainloop()