import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("超高機能電卓")
root.geometry("300x500")

r,c=0,0      #ｒ：行番号　ｃ：列番号
for i in range(9,-1,-1):
    btn=tk.Button(root,
                text=i,
                width=4,
                height=2,
                font=("Times New Roman",30)
                )

    btn.grid(row=r,column=c)
    c+=1
    if (i-1)%3==0:
        r+=1
        c=0
root.mainloop()