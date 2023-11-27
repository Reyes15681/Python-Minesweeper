from graphics import *

win = GraphWin("images", 1000, 1000)
center = Point(500,500)
image = Image(center, "flag.gif")
image.draw(win)

win.getMouse()