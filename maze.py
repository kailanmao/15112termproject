class maze(object):
    def __init__(self, mazeList, app):
        self.mazeList = mazeList
        self.rows = len(self.mazeList)
        self.cols = len(self.mazeList[0])
        self.cellW = app.width // self.cols
        self.cellL = app.height // self.rows
    
    def drawMaze(self, canvas):
        for r in range(self.rows):
            for c in range(self.cols):
                color = "blue" if self.mazeList[r][c] == 1 else "black"
                canvas.create_rectangle(c*self.cellW, r*self.cellL,
                                        (c+1)*self.cellW, (r+1)*self.cellL,
                                        fill=color)
    
    def getCellBounds(self, r, c):
        return (self.cellW*c, self.cellL*r,
                self.cellW*(c+1), self.cellL*(r+1))