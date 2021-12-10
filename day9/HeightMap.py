import tkinter as tk
from day9.Day9Part2 import doWork

#  this class draws a gui containing the height map. It draws all the steps of the recursive algorithm while it's finding all basins. At the end, it marks the three biggest basins in the map
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=800, height=800, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 10
        self.cellheight = 10
        self.result = doWork()
        self.b = self.result[0]
        self.biggestBasin = self.result[1]
        self.count = 0
        self.rect = {}
        for column in range(100):
            for row in range(100):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect")

        self.redraw(2)

    def redraw(self, delay):
        row = self.b[self.count][0]
        col = self.b[self.count][1]
        item_id = self.rect[row, col]
        self.canvas.itemconfig(item_id, fill="green")
        self.count+=1
        print(self.count)
        if self.count< 8500:self.after(delay, lambda: self.redraw(delay))
        else:
            self.count = 0
            self.after(delay, lambda: self.drawBiggestBasin(delay))

    def drawBiggestBasin(self, delay):
        row = self.biggestBasin[self.count][0]
        col = self.biggestBasin[self.count][1]
        item_id = self.rect[row, col]
        self.canvas.itemconfig(item_id, fill="red")
        self.count+=1
        self.after(delay, lambda: self.drawBiggestBasin(delay))

if __name__ == "__main__":
    app = App()
    app.mainloop()