import re
#draw table function and write to file computer.txt for ai player
def drawai(tbldrw=[]):
    def tbl(tbldrw):
        if tbldrw==0: return "0"
        if tbldrw==1: return "1"
        if tbldrw==2: return "2"

    x=5
    print "----------------- "
    while(x>-1):
        print "|",tbl(tbldrw[x][0]),tbl(tbldrw[x][1]),tbl(tbldrw[x][2]),tbl(tbldrw[x][3]),tbl(tbldrw[x][4]),tbl(tbldrw[x][5]),tbl(tbldrw[x][6]),"|"
        x=x-1
    print "----------------- "
    f = open("computer.txt", "w+")
    x=5
    while(x>-1):
        f.write(tbl(tbldrw[x][0]))
        f.write(tbl(tbldrw[x][1]))
        f.write(tbl(tbldrw[x][2]))
        f.write(tbl(tbldrw[x][3]))
        f.write(tbl(tbldrw[x][4]))
        f.write(tbl(tbldrw[x][5]))
        f.write(tbl(tbldrw[x][6]))
        f.write("\n")
        x=x-1
    f.write("2")

#draw table function and write to file human.txt for human player
def drawhu(tbldrw=[]):
    def tbl(tbldrw):
        if tbldrw==0: return "0"
        if tbldrw==1: return "1"
        if tbldrw==2: return "2"
    x=5
    print "----------------- "
    while(x>-1):
        print "|",tbl(tbldrw[x][0]),tbl(tbldrw[x][1]),tbl(tbldrw[x][2]),tbl(tbldrw[x][3]),tbl(tbldrw[x][4]),tbl(tbldrw[x][5]),tbl(tbldrw[x][6]),"|"
        x=x-1
    print "----------------- "
    f = open("human.txt", "w+")
    x=5
    while(x>-1):
        f.write(tbl(tbldrw[x][0]))
        f.write(tbl(tbldrw[x][1]))
        f.write(tbl(tbldrw[x][2]))
        f.write(tbl(tbldrw[x][3]))
        f.write(tbl(tbldrw[x][4]))
        f.write(tbl(tbldrw[x][5]))
        f.write(tbl(tbldrw[x][6]))
        f.write("\n")
        x=x-1
    f.write("1")

#score calculation function
def win(boardstate=[]):
    w1=[1,1,1,1]
    w2=[2,2,2,2]
    a=0
    b=0
    #check horizontal values
    for i in range(6):
        for j in range(4):
            if [boardstate[i][j],boardstate[i][j+1],boardstate[i][j+2],boardstate[i][j+3]]==w1:
                a+=1
            if [boardstate[i][j],boardstate[i][j+1],boardstate[i][j+2],boardstate[i][j+3]]==w2:
                b+=1

    #check vertical values
    for i in range(7):
        for j in range(3):
            if [boardstate[j][i], boardstate[j+1][i], boardstate[j+2][i], boardstate[j+3][i]]==w1:
                a+=1
            if [boardstate[j][i], boardstate[j+1][i], boardstate[j+2][i], boardstate[j+3][i]]==w2:
                b+=1

    #check diagonal values left to right
    for j in range(3):
        for i in range(4):
            if [boardstate[j][i], boardstate[j+1][i+1], boardstate[j+2][i+2], boardstate[j+3][i+3]]==w1:
                a+=1
            if [boardstate[j][i], boardstate[j+1][i+1], boardstate[j+2][i+2], boardstate[j+3][i+3]]==w2:
                b+=1


    #check diagonal values right to left
    for j in range(3):
        for i in range(6,2,-1):
            if [boardstate[j][i], boardstate[j+1][i-1], boardstate[j+2][i-2], boardstate[j+3][i-3]]==w1:
                a+=1
            if [boardstate[j][i], boardstate[j+1][i-1], boardstate[j+2][i-2], boardstate[j+3][i-3]]==w2:
                b+=1
    return a

def winhu(boardstate=[]):
    w1=[1,1,1,1]
    w2=[2,2,2,2]
    a=0
    b=0
    #check horizontal values
    for i in range(6):
        for j in range(4):
            if [boardstate[i][j],boardstate[i][j+1],boardstate[i][j+2],boardstate[i][j+3]]==w1:
                a+=1
            if [boardstate[i][j],boardstate[i][j+1],boardstate[i][j+2],boardstate[i][j+3]]==w2:
                b+=1

    #check vertical values
    for i in range(7):
        for j in range(3):
            if [boardstate[j][i], boardstate[j+1][i], boardstate[j+2][i], boardstate[j+3][i]]==w1:
                a+=1
            if [boardstate[j][i], boardstate[j+1][i], boardstate[j+2][i], boardstate[j+3][i]]==w2:
                b+=1

    #check diagonal values left to right
    for j in range(3):
        for i in range(4):
            if [boardstate[j][i], boardstate[j+1][i+1], boardstate[j+2][i+2], boardstate[j+3][i+3]]==w1:
                a+=1
            if [boardstate[j][i], boardstate[j+1][i+1], boardstate[j+2][i+2], boardstate[j+3][i+3]]==w2:
                b+=1


    #check diagonal values right to left
    for j in range(3):
        for i in range(6,2,-1):
            if [boardstate[j][i], boardstate[j+1][i-1], boardstate[j+2][i-2], boardstate[j+3][i-3]]==w1:
                a+=1
            if [boardstate[j][i], boardstate[j+1][i-1], boardstate[j+2][i-2], boardstate[j+3][i-3]]==w2:
                b+=1
    return b

#check if human move is a valid move
def checkmove(boardstate=[]):
    cols=[]; rows=[]
    for col in range(7):
        for row in range(6):
            if boardstate[row][col]==0:
                cols.append(col)
                rows.append(row)
                break
    return cols, rows
isNum=re.compile("[^0-9]")

#validate human player move and return invalid if error
def hmove(boardstate, col):
    cols, rows = checkmove(boardstate)
    if isNum.match(col)==None and col!='': col=int(col)-1
    while col not in cols:
        print "Invalid move: column is full!!"
        col=raw_input("Re-enter column no. to make your move:")
        if isNum.match(col)==None and col!='': col=int(col)-1
    boardstate[rows[cols.index(col)]][col]=2
