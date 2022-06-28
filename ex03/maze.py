import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")

def key_up(event):
    global key
    key = ""
    #print(f"{key}が離されました")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, 
                       width=1500, 
                       height=900,
                       bg="black")
    canvas.pack()

    tori = tk.PhotoImage(file="fig/6.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()