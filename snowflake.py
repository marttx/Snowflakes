import tkinter as tk
import random
class Snow:
    def __init__(self, canvas):
        self.canvas=canvas
        self.x=random.randint(0, 500)
        self.y=random.randint(0, 500)
        self.size=random.randint(1, 10)
        self.speed=random.randint(0, 5)
        self.id=canvas.create_oval(self.x, self.y, self.x+self.size, self.y+self.size, fill="white", outline="white")
    def place(self):
        self.canvas.move(self.id, 0, self.speed)
        self.y+=self.speed
        if self.y>500:
            self.y=0
            self.x = random.randint(0, 500)
            self.speed = random.randint(0, 5)
            self.canvas.coords(self.id, self.x, self.y, self.x+self.size, self.y+self.size)
class Anim:
    def __init__(self, effect):
        self.effect=effect
        self.canvas=tk.Canvas(effect, width=500, height=500, bg="SteelBlue")
        self.canvas.pack()
        self.lis=[]
        for _ in range(50):
            sn=Snow(self.canvas)
            self.lis.append(sn)
        self.animation()
    def animation(self):
        for sn in self.lis:
            sn.place()
        self.effect.after(50, self.animation)


def main():
    win=tk.Tk()
    a=Anim(win)

    win.mainloop()
if __name__=="__main__":
    main()