from tkinter import *
import settings
import utility
from cell import Cell

#Instantiate a window instance
root=Tk()

#Override the settings of the window
#background color
root.configure(bg="black")

#Adjust the window size. Width x Height
#root.geometry('900x620')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

#title
root.title("Minesweeper Game")

#To disable window resizing. By default window could be resized. False, false stands for width and height
root.resizable(False,False)

#Dividing the window into three frames
#Top Frame
top_frame=Frame(
    root,
    bg="black",
    width=900,
    height=utility.height_percent(25)
)

top_frame.place(x=0,y=0)

#Left Frame
left_frame=Frame(
    root,
    bg="black",
    width=utility.width_percent(25),
    height=utility.height_percent(75)
)

left_frame.place(x=0,y=utility.height_percent(25))


#Center Frame
center_frame=Frame(
    root,
    bg="black",
    width=utility.width_percent(75),
    height=utility.height_percent(75)
)

center_frame.place(x=utility.width_percent(25),y=utility.height_percent(25))


'''#Create Button
btn=Button(
    center_frame,
    bg="white",
    text="button"
    
)

btn.place(x=0,y=0)

c1=Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.place(
    x=0,y=0
)
'''

#Using place method is not a good idea when we need to create multiple cells
#Instead we can use grid
'''
c1=Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(
    column=0,row=0
)
'''
#To create multiple cells
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,row=y
)

#print(Cell.allCells)

#Call count label 
Cell.create_count_cell_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
Cell.randomize_mines()


#Run the window.The program should run until we close it with the X button on the top right.
root.mainloop()