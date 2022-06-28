import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")

def key_up(event):
    global key
    key = ""
    #print(f"{key}が離されました")

def main_proc():
    global mx, my, cx, cy
    delta = {
        "":[0,0],
        "Up":[0,-1],  #キー：押されたキー、値：移動幅リスト[x,y]
        "Down":[0,1],
        "Left":[-1,0],
        "Right":[1,0]}
    mx, my = mx+delta[key][0], my+delta[key][1]
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
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


    tori = tk.PhotoImage(file="fig/6.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()