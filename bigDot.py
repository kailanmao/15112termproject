class bigDot():
    def __init__(self, r, c):
        self.r = r
        self.c = c
    
    def drawBigDot(self, app, canvas):
        x0, y0, x1, y1 = app.maze.getCellBounds(self.r, self.c)
        r = (y1-y0)*1.2
        canvas.create_oval(x0+r, y0+r, x1-r, y1-r, fill="orange")
    
    def __eq__(self, other):
        if not isinstance(other, bigDot):
            return False
        else:
            return self.r == other.r and self.c == other.c
        