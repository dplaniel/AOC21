
def fmred(skk): return "\033[91m{}\033[00m" .format(skk)
def fmpurple(skk): return "\033[95m{}\033[00m" .format(skk)
def fmcyan(skk): return "\033[92m{}\033[00m" .format(skk)

def print_grid(grd, mine, theirs):
    for i in range(grd.shape[0]):
        for j in range(grd.shape[1]):
            elem = grd[i][j]
            if ((i,j) in mine) and ((i,j) in theirs):
                print(fmpurple(elem),end="")
            elif (i,j) in mine:
                print(fmcyan(elem),end="")
            elif (i,j) in theirs:
                print(fmred(elem),end="")
            else:
                print(elem,end="")
        print()