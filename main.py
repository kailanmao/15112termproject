import time
from cmu_112_graphics import *
from maze import *
from pacman import *
from ghost import *
from bigDot import *
from dot import *

def appStarted(app):
    # game things
    app.timerDelay = 300
    app.score = 0
    app.lives = 3
    app.gameOver = False
    app.time = 0
    app.stateStartTime = 0
    app.pause = False
    app.lostLifeStartTime = 0

    # CHANGE LATER - STARTING GHOST STATE
    # app.ghostState = "frightened"

    # maze 2D list
    mazeList = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
                [1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
                [1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1],
                [1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
                [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                [1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],

                [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],

                [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1],
                [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
                [1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1],
                [1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
                [1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    app.maze = maze(mazeList, app)

    # pac man
    pacmanColor = 'yellow'
    pacmanR = 13
    pacmanC = 11
    app.pacman = pacman(pacmanColor, pacmanR, pacmanC, "Up")

    # ghosts
    app.ghost1 = ghost('red', 9, 11)
    app.ghost2 = ghost('pink', 11, 11)
    app.ghost3 = ghost('cyan', 11, 9)
    app.ghost4 = ghost('orange', 11, 13)
    app.ghosts = [app.ghost1, app.ghost2, app.ghost3, app.ghost4]

    # big dots
    app.bigDots = []
    app.bigDotPositions = [(3,4),(3,18),(19,4),(19,18)]
    for r, c in app.bigDotPositions:
        app.bigDots.append(bigDot(r, c))

    # dots
    app.dots = []
    app.dotPositions = []
    ghostHousePositions = [(10,11),(11,9),(11,10),(11,11),(11,12),
                            (11,13)]
    for r in range(len(app.maze.mazeList)):
        for c in range(len(app.maze.mazeList[0])):
            if (app.maze.mazeList[r][c] == 0 and 
                (r,c) not in app.bigDotPositions and
                (r,c) not in ghostHousePositions):
                app.dots.append(dot(r, c))
                app.dotPositions.append((r, c))

def redrawAll(app, canvas):
    # maze - must go first
    app.maze.drawMaze(canvas)

    # score
    canvas.create_text(50, 15, text= f'Score: {app.score}',
                       fill='white', font='Helvetica 20 bold', anchor='w')

    # lives
    for i in range(app.lives):
        x0, y0, x1, y1 = app.maze.getCellBounds(22, i)
        canvas.create_oval(x0+2,y0+2,x1-2,y1-2,fill="yellow")

    # dots and bigDots
    for dot in app.dots:
        dot.drawDot(app,canvas)

    for bigDot in app.bigDots:
        bigDot.drawBigDot(app, canvas)

    # pacman and ghosts
    app.pacman.drawPacman(app, canvas)
    # pacman mouth animation
    if app.time % 3 == 0:
        app.pacman.drawPacmanMouth(app, canvas)

    for ghost in app.ghosts:
        ghost.drawGhost(app, canvas)
    
    # game over screen
    if app.gameOver:
        x0 = app.width // 2 - 200
        y0 = app.height // 2 - 100
        x1 = app.width // 2 + 200
        y1 = app.height // 2 + 100
        canvas.create_rectangle(x0,y0,x1,y1,fill="gold", outline="white")
        if len(app.dots) == 0 and len(app.bigDots) == 0:
            canvas.create_text(app.width // 2, app.height // 2,
            text="YOU WIN\nPress space to play again", fill="green",
            font="Helvetica 30 bold")
        else:
            canvas.create_text(app.width // 2, app.height // 2,
            text="YOU LOSE\nPress space to play again", fill="red3",
            font="Helvetica 30 bold")

def keyPressed(app, event):
    # start over game
    if app.gameOver and event.key == "Space":
        app.lives = 3
        app.score = 0
        app.gameOver = False
        app.time = 0
        app.stateStartTime = 0
        app.pause = False
        app.lostLifeStartTime = 0

    app.pacman.changeDirection(app, event.key)

def timerFired(app):
    app.time += 1
    if app.time - app.lostLifeStartTime == 5 and app.lostLifeStartTime != 0:
        app.pause = False
        app.pacman.r = 13
        app.pacman.c = 11
        app.pacman.direction = "Up"
        for i in range(len(app.ghosts)):
            r, c = app.ghosts[i].startingPositions[i]
            app.ghosts[i].r = r
            app.ghosts[i].c = c

    if app.time - app.stateStartTime == 200 and app.stateStartTime != 0:
        for ghost in app.ghosts:
            if ghost.state == "frightened":
                ghost.state = "chase"

    # MUST GO AFTER TIME CHECKS
    if app.gameOver or app.pause:
        return

    # move pac-man
    app.pacman.move(app)

    # move ghosts
    for ghost in app.ghosts:
        if ghost.state == "frightened":
            ghost.frightenedMove(app)

    # BIG DOT update score and game state
    if (app.pacman.r, app.pacman.c) in app.bigDotPositions:
        app.bigDotPositions.remove((app.pacman.r, app.pacman.c))
        app.bigDots.remove(bigDot(app.pacman.r, app.pacman.c))
        app.score += 50
        app.stateStartTime = app.time
        app.ghostState = "frightened"
        for ghost in app.ghosts:
            ghost.color = "royal blue"
    
    # SMALL DOT update score
    if (app.pacman.r, app.pacman.c) in app.dotPositions:
        app.dotPositions.remove((app.pacman.r, app.pacman.c))
        app.dots.remove(dot(app.pacman.r, app.pacman.c))
        app.score += 10
    
    # contact with ghosts
    for ghost in app.ghosts:
        nextR, nextC = ghost.getNextMove()
        if ((ghost.r == app.pacman.r and ghost.c == app.pacman.c) or
            nextR == app.pacman.r and nextC == app.pacman.c):
            if ghost.color == "royal blue":
                app.score += 200
                # return to normal color and go back to ghost house
                ghostNum = app.ghosts.index(ghost)
                ghost.color = ghost.ghostColors[ghostNum]
                ghost.r, ghost.c = ghost.startingPositions[ghostNum]
            else:
                app.lives -= 1
                app.pause = True
                app.lostLifeStartTime = app.time

    # gameOver conditions
    # win
    if len(app.bigDots) == 0 and len(app.dots) == 0:
        app.gameOver = True
    # lose
    elif app.lives == 0:
        app.gameOver = True

runApp(width=600,height=600)