from maze import *

class pacman(object):
    def __init__(self, color, r, c, dir):
        self.color = color
        self.r = r
        self.c = c
        self.direction = dir
    
    def drawPacman(self, app, canvas):
        x0, y0, x1, y1 = app.maze.getCellBounds(self.r, self.c)
        d = x1 - x0
        canvas.create_oval(x0-d, y0-d, x1+d, y1+d, fill=self.color)
    
    def isLegal(self, app, direction):
        if direction == "Left":
            if (app.pacman.c == 0 and 
                app.pacman.r == app.maze.rows // 2):
                return True
            elif (app.pacman.c > 0 and 
                app.maze.mazeList[app.pacman.r][app.pacman.c - 1] == 0):
                return True
            else:
                return False
        elif direction == "Right":
            if (app.pacman.c == app.maze.cols - 1 and 
                app.pacman.r == app.maze.rows // 2):
                return True
            elif (app.pacman.c < app.maze.cols and 
                app.maze.mazeList[app.pacman.r][app.pacman.c + 1] == 0):
                return True
            else:
                return False
        elif direction == "Down":
            if (app.pacman.r < app.maze.rows and 
                app.maze.mazeList[app.pacman.r + 1][app.pacman.c] == 0):
                return True
            else:
                return False
        elif direction == "Up":
            if (app.pacman.r > 0 and 
                app.maze.mazeList[app.pacman.r - 1][app.pacman.c] == 0):
                return True
            else:
                return False
        else:
            return False

    def changeDirection(self, app, direction):
        if self.isLegal(app, direction):
            self.direction = direction

    def move(self, app):
        if self.isLegal(app, self.direction):
            if self.direction == "Left":
                self.c -= 1
                if self.c <= 0:
                    self.c = app.maze.cols - 1
            elif self.direction == "Right":
                self.c += 1
                if self.c >= app.maze.cols:
                    self.c = 0
            elif self.direction == "Up":
                self.r -= 1
            elif self.direction == "Down":
                self.r += 1
    
    def drawPacmanMouth(self, app, canvas):
        x0, y0, x1, y1 = app.maze.getCellBounds(self.r, self.c)
        d = x1 - x0
        if self.direction == "Up":
            canvas.create_arc(x0-d,y0-d,x1+d,y1+d,width=2,style='pieslice',
                        extent = 60, fill='black', start=60)
        elif self.direction == "Left":
            canvas.create_arc(x0-d,y0-d,x1+d,y1+d,width=2,style='pieslice',
                        extent = 60, fill='black', start=150)
        elif self.direction == "Down":
            canvas.create_arc(x0-d,y0-d,x1+d,y1+d,width=2,style='pieslice',
                        extent = 60, fill='black', start=240)
        else:
            canvas.create_arc(x0-d,y0-d,x1+d,y1+d,width=2,style='pieslice',
                        extent = 60, fill='black', start=330)