from tkinter import Button,Label,messagebox
import random
import settings
import sys

class Cell:
    
    allCells=[]
    cell_count_label_object=None
    cell_count=settings.CELL_COUNT
    
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_open=False
        self.is_mine_candidate=False
        self.cell_btn_object=None
        self.x=x
        self.y=y
        
        #Add cells to the list
        Cell.allCells.append(self)
        
        
    def create_btn_object(self,location):
        btn=Button(
            location,
            width=8,
            height=2,
            #text="Button"
            ##text=f"{self.x},{self.y}"
        )
        
        #Instantiating actions on cells
        btn.bind('<Button-1>',self.left_click_actions) #Left 
        
        btn.bind('<Button-3>',self.right_click_actions) #Right Click
        
        self.cell_btn_object=btn  
        
    
    @staticmethod 
    def create_count_cell_label(location):
        lbl=Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("calibri",20)
        )
        Cell.cell_count_label_object=lbl
        
           
    def left_click_actions(self,event):
        '''print(event)
        print("Left Click")'''
        if self.is_mine:
            self.show_mine()
        else:
            if self.surround_mines==0:
                for cell_ob in self.surrounding_cells:
                    cell_ob.show_cell()
            self.show_cell()
        
        #Game WOn    
        if Cell.cell_count==settings.MINES_COUNT:
            messagebox.showinfo("Congratulations..","You have won the game!!")
        
        #Cancel Left/Right click events on opened cells
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
        
        
    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(
                #bg=SystemButtonFace #for windows
                bg="gainsboro"
            )
            self.is_mine_candidate=False
     
    #Logic when user clicked on mine   
    def show_mine(self):
        self.cell_btn_object.configure(bg="red") 
     
        #self.root.geometry("100x100")  
        messagebox.showerror("GAME OVER!!!","You clicked on a mine") 
        sys.exit()
        
    
    #Logic when user clicked on cell
    def show_cell(self):
        if not self.is_open:
            Cell.cell_count-=1
            self.cell_btn_object.configure(
                text=self.surround_mines
            )
            
            #Replace the count of unopened cells
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
                
            #If cell was a mine candidate, color back to default
            self.cell_btn_object.configure(bg="gainsboro")
            
        self.is_open=True
        
    
    
    def get_cell_coordinates(self,x,y):
        for cell in self.allCells:
            if cell.x==x and cell.y==y:
                return cell
    
    @property 
    def surrounding_cells(self):
        surrounded_cells=[
            self.get_cell_coordinates(self.x-1,self.y-1),
            self.get_cell_coordinates(self.x-1,self.y),
            self.get_cell_coordinates(self.x-1,self.y+1),
            self.get_cell_coordinates(self.x,self.y-1),
            self.get_cell_coordinates(self.x+1,self.y-1),
            self.get_cell_coordinates(self.x+1,self.y),
            self.get_cell_coordinates(self.x+1,self.y+1),
            self.get_cell_coordinates(self.x,self.y+1)
            
        ]
                
        surrounded_cells=[cell for cell in surrounded_cells if cell is not None]
        #print(surrounded_cells)
        return surrounded_cells
    
    @property    
    def surround_mines(self):
        counter=0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter+=1
                
        return counter
    
         
    @staticmethod 
    def randomize_mines():
        mine_cells=random.sample(
            Cell.allCells,settings.MINES_COUNT
        )
        
        for mine_cell in  mine_cells:
            mine_cell.is_mine=True
            
        #print(mine_cells)
        
     
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
         
    
            