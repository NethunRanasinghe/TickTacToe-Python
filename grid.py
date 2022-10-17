from tabulate import tabulate
import os

Grid = []
Column_Index = []

def Clear_Console():
    os.system('cls' if os.name=='nt' else 'clear')

def Initialize_Grid(Grid_Size):
    for j in range(Grid_Size):
        Row = []
        Column_Index.append(j)
        for i in range(Grid_Size):
            Row.append([])
        Grid.append(Row)

    Print_Grid()

def Set_User_Input(Row,Column,Value):
    Clear_Console()
    Grid[Row][Column] = Value
    Print_Grid()

def Print_Grid():
    print(tabulate(Grid,headers=Column_Index, tablefmt='fancy_grid', showindex=True,numalign="center"))