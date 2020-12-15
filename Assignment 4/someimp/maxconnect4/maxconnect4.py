#import statements
from maxconnect4func import *
import sys

#inputfile argument
inputfile = sys.argv[2]

#define table for storing game board state values
table =[]
try:
    myfile = open(inputfile, 'r')
    data = []
    for line in myfile:
        for ch in line:
            if ch != "\n":
                data.append(int(ch))
except IOError:
    sys.exit("\nError opening input file.\nCheck file name.\n")

#populate game board state in table format
p=0
table = [[data[p],data[p+1],data[p+2],data[p+3],data[p+4],data[p+5],data[p+6]],
         [data[p+7],data[p+8],data[p+9],data[p+10],data[p+11],data[p+12],data[p+13]],
         [data[p+14],data[p+15],data[p+16],data[p+17],data[p+18],data[p+19],data[p+20]],
         [data[p+21],data[p+22],data[p+23],data[p+24],data[p+25],data[p+26],data[p+27]],
         [data[p+28],data[p+29],data[p+30],data[p+31],data[p+32],data[p+33],data[p+34]],
         [data[p+35],data[p+36],data[p+37],data[p+38],data[p+39],data[p+40],data[p+41]]]
table.reverse()

#initialize utility function from files
ev1=[int(data0) for data0 in open("data/data0.txt")]
ev2={}
for data1 in open("data/data1.txt"):
    bit=data1.split()
    ev2[int(bit[0])]=int(bit[1])
ev3={}
for data2 in open("data/data2.txt"):
    bit=data2.split()
    ev3[int(bit[0])]=int(bit[1])
ev4={}
for data3 in open("data/data3.txt"):
    bit=data3.split()
    ev4[int(bit[0])]=int(bit[1])
def utility(data4):
    utilvalue=0
    x=0
    while(x<6):
        utilvalue+=ev4[1000000*data4[x][0]+100000*data4[x][1]+10000*data4[x][2]+1000*data4[x][3]+100*data4[x][4]+10*data4[x][5]+data4[x][6]]
        x=x+1
    y=0
    while(y<7):
        utilvalue+=ev3[100000*data4[0][y]+10000*data4[1][y]+1000*data4[2][y]+100*data4[3][y]+10*data4[4][y]+data4[5][y]]
        y=y+1
    utilvalue+=ev3[100000*data4[0][0]+10000*data4[1][1]+1000*data4[2][2]+100*data4[3][3]+10*data4[4][4]+data4[5][5]]
    utilvalue+=ev3[100000*data4[0][1]+10000*data4[1][2]+1000*data4[2][3]+100*data4[3][4]+10*data4[4][5]+data4[5][6]]    
    utilvalue+=ev3[100000*data4[5][1]+10000*data4[4][2]+1000*data4[3][3]+100*data4[2][4]+10*data4[1][5]+data4[0][6]]
    utilvalue+=ev3[100000*data4[5][0]+10000*data4[4][1]+1000*data4[3][2]+100*data4[2][3]+10*data4[1][4]+data4[0][5]]    
    utilvalue+=ev2[10000*data4[1][0]+1000*data4[2][1]+100*data4[3][2]+10*data4[4][3]+data4[5][4]]
    utilvalue+=ev2[10000*data4[0][2]+1000*data4[1][3]+100*data4[2][4]+10*data4[3][5]+data4[4][6]]
    utilvalue+=ev2[10000*data4[4][0]+1000*data4[3][1]+100*data4[2][2]+10*data4[1][3]+data4[0][4]]
    utilvalue+=ev2[10000*data4[5][2]+1000*data4[4][3]+100*data4[3][4]+10*data4[2][5]+data4[1][6]]
    utilvalue+=ev1[27*data4[0][3]+9*data4[1][4]+3*data4[2][5]+data4[3][6]]
    utilvalue+=ev1[27*data4[2][0]+9*data4[3][1]+3*data4[4][2]+data4[5][3]]
    utilvalue+=ev1[27*data4[3][0]+9*data4[2][1]+3*data4[1][2]+data4[0][3]]
    utilvalue+=ev1[27*data4[5][3]+9*data4[4][4]+3*data4[3][5]+data4[2][6]]
    return utilvalue

#function to check for valid move for ai
colnmber=[2,3,1,4,0,6,5]
def checkmove(tabledata):
    global colnmber
    column=[]
    for i in colnmber:
        for j in range(6):
            if tabledata[j][i]==0:
                column.append([j,i])
                break
    return column

#place move and set next player
def playturn(tabledata,y,next):
    val=checkmove(tabledata)
    tabledata[val[y][0]][val[y][1]]=next

##min max algorithm with first,beta for calculating next move
def minimax(tabledata, diff):
    def minmaxmain(tabledata, diff, first, second):
        elements=[];  inf=-10000000
        for p,q in checkmove(tabledata):
            tabledata[p][q]=1
            inf=max(inf, amin(tabledata, diff-1, first, second))
            elements.append(inf)
            tabledata[p][q]=0
        if not elements:
            drawaione(table)
            ag = win(table)
            hu = winhu(table)
            if ag==hu:
                print "Score: AI Agent =",ag,", Player =",hu
                print ""
            else:
                print "Score: AI Agent =",ag,", Player =",hu
                print ""
        else:
            infinity=max(elements)
            index1=elements.index(infinity)
            return [index1, infinity]
    def amax(tabledata, diff, first, second):
        column=checkmove(tabledata)
        if(diff==0 or not column):
            return utility(tabledata)
        inf=-10000000
        for p,q in column:
            tabledata[p][q]=1
            inf=max(inf, amin(tabledata, diff-1, first, second))
            tabledata[p][q]=0
            if inf >= second: return inf
            first=max(first, inf)
        return inf
    def amin(tabledata, diff, first, second):
        column=checkmove(tabledata)
        if(diff==0 or not column):
            return utility(tabledata)
        inf=+10000000
        for p,q in column:
            tabledata[p][q]=2
            inf=min(inf, amax(tabledata, diff-1, first, second))
            tabledata[p][q]=0
            if inf <= first: return inf
            second=min(second, inf)
        return inf    
    return minmaxmain(tabledata, diff, -10000000, +10000000)
def searchmove(tabledata):
    global colnmber
    diff=1
    reach=minimax(tabledata, depp)
    try:
        return reach[0]
    except TypeError:
        sys.exit(1)
        
#read arguments and initialize game state
agent=0; player=0
gamemode = sys.argv[1]
first = sys.argv[3]
dep = sys.argv[4]
depp = int(dep)
if gamemode == 'one-move' or gamemode == 'interactive':
    print ""
else:
    print('%s is an unrecognized game mode' % gamemode)
    sys.exit(1)
def drawaione(tbldrw=[]):
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
    f = open(first, "w+")
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
    
if gamemode == 'one-move':
    print "Player 1 = Disc 1 , Opponent = Disc 2"
    print ""
    print "Current board state:"
    drawaione(table)
    if data[42] == 1:
        print "Player 1's move:"
        playturn(table, searchmove(table), 1)
    if data[42] == 2:
        print "Not making a move as it is opponent player's turn:"
    drawaione(table)

    #read game mode and select first player
if gamemode == 'interactive':
    if first == 'human-next' or first == 'computer-next':
        print ""
    else:
        print('%s is an unrecognized first player name' % first)
        sys.exit(1)
    if first=='human-next':
        print "AI Agent = Disc 1 , Human Player = Disc 2"
        print ""
        print "Current board state:"
        drawhu(table)    
        while checkmove(table):
            ag = win(table)
            hu = winhu(table)
            if ag==hu: print "Score: AI Agent =",ag,", Player =",hu
            else: print "Score: AI Agent =",ag,", Player =",hu
            n=raw_input("Enter column no. to make your move: ")
            hmove(table, n)
            drawhu(table)
            playturn(table, searchmove(table), 1)
            print "AI Agent's Move:"
            drawai(table)
    else:
        print "AI Agent = Disc 1 , Human Player = Disc 2"
        print ""
        print "Current board state:"
        while checkmove(table):            
            drawai(table)
            playturn(table, searchmove(table), 1)
            print "AI Agent's Move:"
            drawai(table)
            ag = win(table)
            hu = winhu(table)
            if ag==hu: print "Score: AI Agent =",ag,", Player =",hu
            else: print "Score: AI Agent =",ag,", Player =",hu
            n=raw_input("Enter column no. to make your move: ")
            print "Player's move:"
            hmove(table, n)
            drawhu(table)

#count score and print
ag = win(table)
hu = winhu(table)
if ag==hu: print "Score: AI Agent =",ag,", Player =",hu
else: print "Score: AI Agent =",ag,", Player =",hu
