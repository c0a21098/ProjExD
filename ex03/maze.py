import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random
def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")

def key_up(event):
    global key
    key = ""
    #print(f"{key}が離されました")

def main_proc():
    global mx, my, cx, cy, tori
    delta = {
        "":[0,0],
        "Up":[0,-1],  #キー：押されたキー、値：移動幅リスト[x,y]
        "Down":[0,1],
        "Left":[-1,0],
        "Right":[1,0]}
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]]==0:
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    if cx==13*100+50 and cy==7*100+50:
        label=tk.Label(root,text="ゲームクリア",font=("Times",20))
        tkm.showinfo("おめでとう","ゲームクリアです")
        return
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(
                    root, 
                    width=1500, 
                    height=900,
                    bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)
    #print(maze_bg)
    

    tori = tk.PhotoImage(file=f"fig/{random.randint(0,9)}.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")
    canvas.create_text(cx,cy,text="START",anchor="center",font=("Times",20))
    canvas.create_text(13*100+50,7*100+50,text="GOAL",anchor="center",font=("Times",20))
    key = ""


    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()


    root.mainloop()