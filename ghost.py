import random
import copy

class ghost():

    ghostColors = ["red", "pink", "cyan", "orange"]
    startingPositions = [(9,11), (11,11), (11,9), (11,13)]
    directions = ["Down","Up", "Right", "Left"]
    directionChanges = [(1,0), (-1,0), (0,1), (0,-1)]

    # where to scatter to with Dijkstra's alg
    scatterTargets = []

    # change default state later
    def __init__(self, color, r, c, state="frightened", direction="Up"):
        self.color = color
        self.r = r
        self.c = c
        self.direction = direction
        self.state = state
    
    def drawGhost(self, app, canvas):
        # body
        x0, y0, x1, y1 = app.maze.getCellBounds(self.r, self.c)
        canvas.create_arc(x0, y0, x1, y1, fill=self.color, style="pieslice",
                            extent=180, start=0, outline=self.color)
        cellWidth = y1 - y0

        y0 += (y1 - y0) // 2
        y1 = y0 + (y1 - y0) // 4 + 5
        canvas.create_rectangle(x0, y0, x1, y1, fill=self.color,
                                outline=self.color)
        
        # tentacles
        canvas.create_arc(x0, y0, x0+cellWidth//3, y0+cellWidth//2,
                            fill=self.color, style="pieslice",
                            extent=180, start=180, outline=self.color)
        canvas.create_arc(x0+cellWidth//3, y0, x0+2*(cellWidth//3),
                            y0+cellWidth//2, fill=self.color,
                            style="pieslice", extent=180, start=180,
                            outline=self.color)
        canvas.create_arc(x0+2*(cellWidth//3), y0, x0+cellWidth,
                            y0+cellWidth//2, fill=self.color,
                            style="pieslice", extent=180, start=180,
                            outline=self.color)
        
        # eyes
        canvas.create_oval(x0+cellWidth//4, y0-5, x0+cellWidth//4+cellWidth//5,
                            y0-5+cellWidth//5, fill="white", outline="white")
        canvas.create_oval(x0+3*(cellWidth//4), y0-5, 
                            x0+3*(cellWidth//4)+cellWidth//5, y0-5+cellWidth//5,
                            fill="white", outline="white")
        
        eyeWidth = (x0+cellWidth//4+cellWidth//5) - (x0+cellWidth//4)
        pupilWidth = eyeWidth // 2
        canvas.create_oval(x0+cellWidth//4+pupilWidth, y0-5+pupilWidth,
                            x0+cellWidth//4+cellWidth//5-pupilWidth,
                            y0-5+cellWidth//5-pupilWidth,
                            fill="black", outline="black")
        canvas.create_oval(x0+3*(cellWidth//4)+pupilWidth, y0-5+pupilWidth, 
                            x0+3*(cellWidth//4)+cellWidth//5-pupilWidth,
                            y0-5+cellWidth//5-pupilWidth,
                            fill="black", outline="black")
    
    def isLegal(self, app, direction):
        if direction == "Left":
            if (self.c > 0 and 
                app.maze.mazeList[self.r][self.c - 1] == 0):
                return True
            else:
                return False
        elif direction == "Right":
            if (self.c < app.maze.cols and 
                app.maze.mazeList[self.r][self.c + 1] == 0):
                return True
            else:
                return False
        elif direction == "Down":
            if (self.r < app.maze.rows and 
                app.maze.mazeList[self.r + 1][self.c] == 0):
                return True
            else:
                return False
        elif direction == "Up":
            if (self.r > 0 and 
                app.maze.mazeList[self.r - 1][self.c] == 0):
                return True
            else:
                return False

    # make sure ghosts can't "skip" over pacman
    def getNextMove(self):
        dirIndex = ghost.directions.index(self.direction)
        dr, dc = ghost.directionChanges[dirIndex]
        return self.r + dr, self.c + dc

    # just move randomly, don't go backwards unless necessary
    def frightenedMove(self, app):
        if self.isLegal(app, self.direction):
            if self.direction == "Left":
                self.c -= 1
            elif self.direction == "Right":
                self.c += 1
            elif self.direction == "Up":
                self.r -= 1
            elif self.direction == "Down":
                self.r += 1
        else:
            randomNum = random.randint(0,3)
            self.direction = ghost.directions[randomNum]

    def predictPacmanMove(self, pacman, steps):
        # steps: how many steps ahead
        # pink ghost: 4
        # blue ghost: 2 i think????????
        pass

    def seekTarget(self, app, targetR, targetC):
        # based on Dijkstra's path to target, RETURN best direction
        # scatter and chase will both use this function
        pass

    def scatterMove(self, app):
        # use dijkstra's to move to 4 corners
        pass

    def chaseMove(self, app):
        pass