import logic as Lg
import grid as GD

G_Size = 0
G_Row = 0
G_Column = 0
G_Turn = 0
G_TurnType = ""

#Get user input and Set Grid Size
G_Size = int(input("Enter Grid Size : "))
GD.Initialize_Grid(G_Size)

#Get User Input on values
while Lg.Validation(G_Row,G_Column,G_Turn) == True :
    G_UInput = input("Enter your position :: row,column :- ")
    G_Row = int(G_UInput.split(',')[0])
    G_Column = int(G_UInput.split(',')[1])

    if (G_Turn % 2 == 0):
        G_TurnType = "X"
    else:
        G_TurnType = "O"

    GD.Set_User_Input(G_Row,G_Column,G_TurnType)

    G_Turn += 1