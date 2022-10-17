import grid as GD

def Validation(Row_Check,Column_Check,Turn_Check):

    if(Turn_Check == (len(GD.Grid) * len(GD.Grid))):
        return False

    return True