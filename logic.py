import grid as GD

def Validation(Row_Check,Column_Check,Turn_Check):

    if(Turn_Check == (len(GD.Grid) * len(GD.Grid))):
        return False

    D_Left = Column_Check - 0
    D_Right = (len(GD.Grid) - 1) - Column_Check
    D_Top = Row_Check - 0
    D_Bottom = (len(GD.Grid) - 1) - Row_Check

    if(Win_Logic(D_Left,D_Right,D_Top,D_Bottom,Row_Check,Column_Check)):
        print("You Won !")
        return False

    return True


def Win_Logic(DL,DR,DT,DB,R_V,C_V):
    win = 0

    #Horizontal win check
    if DL > 0:
        S_Count_H = 0
        for i in range(len(GD.Grid) - 1):
            if(GD.Grid[R_V][i] == GD.Grid[R_V][i + 1]):
                S_Count_H += 1
                if(S_Count_H == (len(GD.Grid) - 1)):
                    win = 1
                    print("Horizontal win")
            else:
                break
    
    #Vertical win check
    if DT > 0:
        S_Count_V = 0
        for i in range(len(GD.Grid) - 1):
            if(GD.Grid[i][C_V] == GD.Grid[i + 1][C_V]):
                S_Count_V += 1
                if(S_Count_V == (len(GD.Grid) -1 )):
                    win = 1
            else:
                break

    #Diagonal right win check
    if(GD.Grid[0][len(GD.Grid) - 1] == "X" or GD.Grid[0][len(GD.Grid) - 1] == "O"):
        if (GD.Grid[0][len(GD.Grid) - 1] == GD.Grid[R_V][C_V]):
            S_Count_DR = 0
            for i in range(len(GD.Grid) - 1):
                if(GD.Grid[i][len(GD.Grid) - (i+1)] == GD.Grid[i + 1][len(GD.Grid) - (i+2)]):
                    S_Count_DR += 1
                    if(S_Count_DR == (len(GD.Grid) - 1)):
                        win = 1
                else:
                    break

    #Diagonal left win check
    if(GD.Grid[0][0] == "X" or GD.Grid[0][0] == "O"):
        if (GD.Grid[0][0] == GD.Grid[R_V][C_V]):
            S_Count_DL = 0
            for i in range(len(GD.Grid) - 1):
                if(GD.Grid[i][i] == GD.Grid[i + 1][i + 1]):
                    S_Count_DL += 1
                    if(S_Count_DL == (len(GD.Grid) - 1)):
                        win = 1
                else:
                    break
    
    if win == 1:
        return True

    return False