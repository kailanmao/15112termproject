import random

class ghost():

    ghostColors = ["red", "pink", "cyan", "orange"]
    startingPositions = [(31,34), (34,34), (34,28), (34,40)]
    directions = ["Right","Up", "Left", "Down"]
    directionChanges = [(0,1), (-1,0), (0,-1), (1,0)]

    def __init__(self, color, r, c, timeInterval, state="chase", direction="Up"):
        self.color = color
        self.r = r
        self.c = c
        self.direction = direction
        self.state = state
        self.path = []
        self.timeInterval = timeInterval
    
    def drawGhost(self, app, canvas):
        # body
        x0, y0, x1, y1 = app.maze.getCellBounds(self.r, self.c)
        d = x1 - x0
        canvas.create_arc(x0-d, y0-d, x1+d, y1+d, fill=self.color, style="pieslice",
                            extent=180, start=0, outline=self.color)
        cellWidth = 3*(y1 - y0)

        y0 += (y1 - y0) // 2
        y1 = y0 + (y1 - y0) // 4
        canvas.create_rectangle(x0-d, y0, x1+d, y1+d, fill=self.color,
                                outline=self.color)
        
        # tentacles
        canvas.create_arc(x0-d, y0, x0+cellWidth//3-d, y0+cellWidth//2,
                            fill=self.color, style="pieslice",
                            extent=180, start=180, outline=self.color)
        canvas.create_arc(x0+cellWidth//3-d, y0, x0+2*(cellWidth//3)-d,
                            y0+cellWidth//2, fill=self.color,
                            style="pieslice", extent=180, start=180,
                            outline=self.color)
        canvas.create_arc(x0+2*(cellWidth//3)-d, y0, x0+cellWidth-d,
                            y0+cellWidth//2, fill=self.color,
                            style="pieslice", extent=180, start=180,
                            outline=self.color)
        
        # eyes
        canvas.create_oval(x0+cellWidth//4-d, y0-5, 
                            x0+cellWidth//4+cellWidth//5-d,
                            y0-5+cellWidth//5, fill="white", outline="white")
        canvas.create_oval(x0+3*(cellWidth//4)-d, y0-5, 
                            x0+3*(cellWidth//4)+cellWidth//5-d,
                            y0-5+cellWidth//5,
                            fill="white", outline="white")
        
        eyeWidth = (x0+cellWidth//4+cellWidth//5) - (x0+cellWidth//4)
        pupilWidth = eyeWidth // 2
        canvas.create_oval(x0+cellWidth//4+pupilWidth-d, y0-5+pupilWidth,
                            x0+cellWidth//4+cellWidth//5-pupilWidth-d,
                            y0-5+cellWidth//5-pupilWidth,
                            fill="black", outline="black")
        canvas.create_oval(x0+3*(cellWidth//4)+pupilWidth-d, y0-5+pupilWidth, 
                            x0+3*(cellWidth//4)+cellWidth//5-pupilWidth-d,
                            y0-5+cellWidth//5-pupilWidth,
                            fill="black", outline="black")
    
    def isLegal(self, r,c,app, direction):
        if direction == "Left":
            if (c > 0 and 
                app.maze.mazeList[r][c - 1] == 0):
                return True
            else:
                return False
        elif direction == "Right":
            if (c < app.maze.cols and 
                app.maze.mazeList[r][c + 1] == 0):
                return True
            else:
                return False
        elif direction == "Down":
            if (r < app.maze.rows and 
                app.maze.mazeList[r + 1][c] == 0):
                return True
            else:
                return False
        elif direction == "Up":
            if (r > 0 and 
                app.maze.mazeList[r - 1][c] == 0):
                return True
            else:
                return False

    # make sure ghosts can't "skip" over pacman
    def getNextMove(self):
        dirIndex = ghost.directions.index(self.direction)
        dr, dc = ghost.directionChanges[dirIndex]
        return self.r + dr, self.c + dc

    def getPossibleDirections(self,app):
        dirs = []
        for dr,dc in self.directionChanges:
            if app.maze.mazeList[self.r+dr][self.c+dc] == 0:
                dirs.append((dr,dc))
        return dirs

    def getOppositeDirection(self):
        if self.direction == "Left":
            return 0
        elif self.direction == "Right":
            return 2
        elif self.direction == "Up":
            return 3
        else:
            return 1

    def frightenedMove(self, app):
        dirs = self.getPossibleDirections(app)
        if len(dirs)==1:
            i = self.directionChanges.index(dirs[0])
            self.direction = self.directions[i]
        else:
            oppDir = self.getOppositeDirection()
            if self.directionChanges[oppDir] in dirs:
                dirs.remove(self.directionChanges[oppDir])
            newDir = dirs[random.randint(0,len(dirs)-1)]
            newDirIndex = self.directionChanges.index(newDir)
            self.direction = self.directions[newDirIndex]
        
        if self.direction == "Left":
            self.c -= 1
        elif self.direction == "Right":
            self.c += 1
        elif self.direction == "Up":
            self.r -= 1
        elif self.direction == "Down":
            self.r += 1

    def backtrack(self,app):
        targetR, targetC = app.pacman.r, app.pacman.c
        return self.backtrackHelper(app,{(self.r,self.c)},[(self.r,self.c)],targetR,targetC)

    def backtrackHelper(self,app,visited,solution,targetR,targetC,depth=0):
        if solution[-1] == (targetR,targetC):
            return solution
        else:
            for i in range(len(self.directions)):

                r,c = solution[-1]
                dr,dc = self.directionChanges[i]
                if self.isLegal(r,c,app,self.directions[i]) and (r+dr,c+dc) not in visited:
                    solution.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
                    newSol = self.backtrackHelper(app,visited,solution,targetR,targetC,depth+1)
                    if newSol != None:
                        return newSol
                    else:
                        solution.pop()
                        visited.remove((r+dr,c+dc))
            return None