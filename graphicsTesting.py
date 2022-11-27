from cmu_112_graphics import *

def redrawAll(app, canvas):
    # pacman mouth when facing right
    canvas.create_arc(100,100,200,200,outline='black', width=5,style='pieslice',
                        extent = 60, fill='black', start=330)



runApp(width=600,height=600)