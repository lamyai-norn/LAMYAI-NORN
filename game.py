import tkinter as tk 
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("980x630")
#veriable for stalled
# 1 is the player
# 2 are the walls
grid = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
frame=tk.Frame()
frame.master.title("hello gamer")
#condition
position1=True
#ball1
direction_x1=410
direction_y1=0
#Function
def drawGrid():
    for col in range(len(grid)):
        y1=col*70
        y2=y1+70
        for row in range(len(grid[0])):
            x1=row*70
            x2=x1+70
            if grid[col][row]!=1:
                color="white"
            else:
                color="black"
            player=canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    return None
def moveToLeft(event):
    global grid 
    indexX=-1
    indexY=-1
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                indexX=row
                indexY=col
    if  indexX>0:
        grid[indexY][indexX]=0
        grid[indexY][indexX-1]=1
    drawGrid()
    
def moveToRight(event):
    global grid
    indexX=-1
    indexY=-1
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                indexX=row
                indexY=col
    if indexX<len(grid)-1:
        grid[indexY][indexX]=0
        grid[indexY][indexX+1]=1
    drawGrid()
def moveToUp(event):
    global grid
    indexX=-1
    indexY=-1
    for col in range(len(grid)):
        for row in range(len(grid[0])):
           if grid[col][row]==1:
               indexX=row
               indexY=col
    if  indexY>0:
        grid[indexY][indexX]=0
        grid[indexY-1][indexX]=1
    drawGrid()
def moveToDown(event):
    global grid
    indexX=-1
    indexY=-1
    for  col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row]==1:
                indexX=row
                indexY=col
    if indexY<len(grid)-1:
        grid[indexY][indexX]=0
        grid[indexY+1][indexX]=1
    drawGrid()
canvas=tk.Canvas(root)
root.bind("<Left>",moveToLeft)#move to left
root.bind("<Right>",moveToRight)#move to right
root.bind("<Up>",moveToUp)#move to up
root.bind("<Down>",moveToDown)#move to down

canvas.pack(expand=True,fill='both')
drawGrid()
root.resizable(False,False)
root.mainloop()
