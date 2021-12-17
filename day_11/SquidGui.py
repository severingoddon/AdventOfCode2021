import tkinter as tk
from tkinter import *
import copy
#  this class draws a gui containing the height map. It draws all the steps of the recursive algorithm while it's finding all basins. At the end, it marks the three biggest basins in the map
from day_11.Day11bothParts import doWork


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=800, height=800, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 50
        self.cellheight = 50
        self.count = 0
        self.lastSteps = []
        self.algoSteps = doWork()
        self.rect = {}
        for column in range(10):
            for row in range(10):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="black", tags="rect")
                self.rect[row,column] = self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="gray13")
        self.text = self.canvas.create_text(300, 600, fill="darkblue", font="Times 14 italic bold",text=".")
        self.redraw(200)

    def redraw(self, delay):
        self.canvas.itemconfig(self.text,text="step:"+str(self.count))
        print(self.count)
        steps = self.algoSteps[self.count]
        for step in steps:
            item_id = self.rect[step[0], step[1]]
            self.canvas.itemconfig(item_id, fill="white")
        if len(self.lastSteps) > 0:
            for step in self.lastSteps:
                item_id = self.rect[step[0], step[1]]
                self.canvas.itemconfig(item_id, fill="gray13")
        self.lastSteps = copy.deepcopy(steps)
        self.count += 1
        steps.clear()

        self.after(delay, lambda: self.redraw(delay))


if __name__ == "__main__":
    app = App()
    app.mainloop()