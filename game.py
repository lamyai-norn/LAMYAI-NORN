import tkinter as tk 
#make empty window
root=tk.Tk()
# put screenwidth and 
root.geometry("800x800")
#veriable for stalled
grid = [[1,0,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0]]
frame=tk.Frame()
frame.master.title("hello gamer")
#condition
position1=True
#ball1
direction_x1=410
direction_y1=0
#Function
def moveBall1():
    global grid,direction_x1,direction_y1,position1,ball1
    canvas.moveto(ball1,direction_x1,direction_y1)
    if direction_y1>=0 and direction_y1<=790 and  position1==True:
        direction_y1+=5
        canvas.after(10,lambda:moveBall1(ball1))
    else:
        position1=False
        direction_y1-=5
        canvas.after(10,lambda:moveBall1(ball1))
        if direction_y1==0:
            condition=True
def drawGrid():
    for col in range(len(grid)):
        y1=col*80
        y2=y1+80
        for row in range(len(grid[0])):
            x1=row*80
            x2=x1+80
            if grid[col][row]!=1:
                color="white"
            else:
                color="black"
            player=canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    canvas.create_rectangle(160,160,240,400,fill="red")
    canvas.create_rectangle(160,80,480,160,fill="red")
    canvas.create_rectangle(320,240,400,480,fill="red")
    canvas.create_rectangle(79,640,400,720,fill="red")
    canvas.create_rectangle(0,480,240,560,fill="red")
    canvas.create_rectangle(560,480,640,800,fill="red")
    canvas.create_rectangle(480,240,720,320,fill="red")
    ball1=canvas.create_oval(410,10,470,60,fill="green")
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
#move ball
canvas.after(1000,lambda:moveBall1(ball1))
canvas.pack(expand=True,fill='both')
drawGrid()
root.resizable(False,False)
root.mainloop()
