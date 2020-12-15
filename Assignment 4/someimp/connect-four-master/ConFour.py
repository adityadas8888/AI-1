from Con4Utils import *
import sys
##table = [[0, 0, 0, 1, 0, 0, 0],
##	 [0, 0, 0, 2, 0, 0, 0],
##	 [0, 0, 0, 3, 0, 0, 0],
##	 [0, 0, 0, 4, 0, 0, 0],
##	 [0, 0, 0, 5, 0, 0, 0],
##	 [0, 0, 0, 6, 0, 0, 0]]
inputfile = sys.argv[2]

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

p=0
##table[0]=[[data[p],data[p+1],data[p+2],data[p+3],data[p+4],data[p+5],data[p+6]]
##table[1]=[[data[p+8],data[p+9],data[p+10],data[p+11],data[p+12],data[p+13],data[p+14]]
##table[2]=[[data[p+16],data[p+17],data[p+18],data[p+19],data[p+20],data[p+21],data[p+22]]
##table[3]=[[data[p+24],data[p+25],data[p+26],data[p+27],data[p+28],data[p+29],data[p+30]]
##table[4]=[[data[p+32],data[p+33],data[p+34],data[p+35],data[p+36],data[p+37],data[p+38]]
##table[5]=[[data[p+40],data[p+41],data[p+42],data[p+43],data[p+44],data[p+45],data[p+46]]

table = [[data[p],data[p+1],data[p+2],data[p+3],data[p+4],data[p+5],data[p+6]],
         [data[p+7],data[p+8],data[p+9],data[p+10],data[p+11],data[p+12],data[p+13]],
         [data[p+14],data[p+15],data[p+16],data[p+17],data[p+18],data[p+19],data[p+20]],
         [data[p+21],data[p+22],data[p+23],data[p+24],data[p+25],data[p+26],data[p+27]],
         [data[p+28],data[p+29],data[p+30],data[p+31],data[p+32],data[p+33],data[p+34]],
         [data[p+35],data[p+36],data[p+37],data[p+38],data[p+39],data[p+40],data[p+41]]]

table.reverse()

l4=[int(i) for i in open("eval/ev_table.txt")]

l5={}
for li in open("eval/5ki.txt"):
    tok=li.split()
    l5[int(tok[0])]=int(tok[1])

l6={}
for li in open("eval/6ki.txt"):
    tok=li.split()
    l6[int(tok[0])]=int(tok[1])

l7={}
for li in open("eval/7ki.txt"):
    tok=li.split()
    l7[int(tok[0])]=int(tok[1])

#Evaluation Method, uses the hash tables to evalutate lines
def eval(t):
    evaluation=0
    evaluation+=l7[1000000*t[0][0]+100000*t[0][1]+10000*t[0][2]+1000*t[0][3]+100*t[0][4]+10*t[0][5]+t[0][6]]
    evaluation+=l7[1000000*t[1][0]+100000*t[1][1]+10000*t[1][2]+1000*t[1][3]+100*t[1][4]+10*t[1][5]+t[1][6]]
    evaluation+=l7[1000000*t[2][0]+100000*t[2][1]+10000*t[2][2]+1000*t[2][3]+100*t[2][4]+10*t[2][5]+t[2][6]]
    evaluation+=l7[1000000*t[3][0]+100000*t[3][1]+10000*t[3][2]+1000*t[3][3]+100*t[3][4]+10*t[3][5]+t[3][6]]
    evaluation+=l7[1000000*t[4][0]+100000*t[4][1]+10000*t[4][2]+1000*t[4][3]+100*t[4][4]+10*t[4][5]+t[4][6]]
    evaluation+=l7[1000000*t[5][0]+100000*t[5][1]+10000*t[5][2]+1000*t[5][3]+100*t[5][4]+10*t[5][5]+t[5][6]]

    evaluation+=l6[100000*t[0][0]+10000*t[1][0]+1000*t[2][0]+100*t[3][0]+10*t[4][0]+t[5][0]]
    evaluation+=l6[100000*t[0][1]+10000*t[1][1]+1000*t[2][1]+100*t[3][1]+10*t[4][1]+t[5][1]]
    evaluation+=l6[100000*t[0][2]+10000*t[1][2]+1000*t[2][2]+100*t[3][2]+10*t[4][2]+t[5][2]]
    evaluation+=l6[100000*t[0][3]+10000*t[1][3]+1000*t[2][3]+100*t[3][3]+10*t[4][3]+t[5][3]]
    evaluation+=l6[100000*t[0][4]+10000*t[1][4]+1000*t[2][4]+100*t[3][4]+10*t[4][4]+t[5][4]]
    evaluation+=l6[100000*t[0][5]+10000*t[1][5]+1000*t[2][5]+100*t[3][5]+10*t[4][5]+t[5][5]]
    evaluation+=l6[100000*t[0][6]+10000*t[1][6]+1000*t[2][6]+100*t[3][6]+10*t[4][6]+t[5][6]]

    evaluation+=l6[100000*t[0][0]+10000*t[1][1]+1000*t[2][2]+100*t[3][3]+10*t[4][4]+t[5][5]]
    evaluation+=l6[100000*t[0][1]+10000*t[1][2]+1000*t[2][3]+100*t[3][4]+10*t[4][5]+t[5][6]]    
    evaluation+=l6[100000*t[5][1]+10000*t[4][2]+1000*t[3][3]+100*t[2][4]+10*t[1][5]+t[0][6]]
    evaluation+=l6[100000*t[5][0]+10000*t[4][1]+1000*t[3][2]+100*t[2][3]+10*t[1][4]+t[0][5]]
    
    evaluation+=l5[10000*t[1][0]+1000*t[2][1]+100*t[3][2]+10*t[4][3]+t[5][4]]
    evaluation+=l5[10000*t[0][2]+1000*t[1][3]+100*t[2][4]+10*t[3][5]+t[4][6]]
    evaluation+=l5[10000*t[4][0]+1000*t[3][1]+100*t[2][2]+10*t[1][3]+t[0][4]]
    evaluation+=l5[10000*t[5][2]+1000*t[4][3]+100*t[3][4]+10*t[2][5]+t[1][6]]
    evaluation+=l4[27*t[0][3]+9*t[1][4]+3*t[2][5]+t[3][6]]
    evaluation+=l4[27*t[2][0]+9*t[3][1]+3*t[4][2]+t[5][3]]
    evaluation+=l4[27*t[3][0]+9*t[2][1]+3*t[1][2]+t[0][3]]
    evaluation+=l4[27*t[5][3]+9*t[4][4]+3*t[3][5]+t[2][6]]
    return evaluation

#valid moves
order=[3,2,4,1,5,0,6]
def validMoves(intable):
    global order
    moves=[]
    for col in order:
        for row in range(6):
            if intable[row][col]==0:
                moves.append([row,col])
                break
    return moves

#moves in slot x acording to valid moves function
def move(intable,x,who):
    val=validMoves(intable)
    intable[val[x][0]][val[x][1]]=who

#Alpha Beta Pruning Search Algorithm
def alphabetaPruning(intable, depth):
    def ab(intable, depth, alpha, beta):
        values=[];  v=-10000000
        for a,s in validMoves(intable):
            intable[a][s]=1
            v=max(v, abmin(intable, depth-1, alpha, beta))
            values.append(v)
            intable[a][s]=0
        largest=max(values)
        dex=values.index(largest)
        return [dex, largest]

    def abmax(intable, depth, alpha, beta):
        moves=validMoves(intable)
        if(depth==0 or not moves):
            return eval(intable)

        v=-10000000
        for a,s in moves:
            intable[a][s]=1
            v=max(v, abmin(intable, depth-1, alpha, beta))
            intable[a][s]=0
            if v >= beta: return v
            alpha=max(alpha, v)
        return v

    def abmin(intable, depth, alpha, beta):
        moves=validMoves(intable)
        if(depth==0 or not moves):
            return eval(intable)

        v=+10000000
        for a,s in moves:
            intable[a][s]=2
            v=min(v, abmax(intable, depth-1, alpha, beta))
            intable[a][s]=0
            if v <= alpha: return v
            beta=min(beta, v)
        return v
    
    return ab(intable, depth, -10000000, +10000000)

#Iterative Deepening Search Algorithm
def iterDeepening(intable):
    global order
    depth=1
    res=alphabetaPruning(intable, depp)
    while True:
        if abs(res[1])>5000: #terminal node
            print ""
            return res[0] 
        tmp=res[0]
        #chaning the order in considering moves
        while tmp!=0:
            order[tmp-1],order[tmp]=order[tmp],order[tmp-1]
            tmp-=1
        depth+=1
        res=alphabetaPruning(intable, depp)
        return res[0]
        
#GAME
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
    

if gamemode == 'one-move':
    print "Current board state:"
    drawaione(table)
    move(table, iterDeepening(table), 1)
    print "Player AI Agent's Move:"
    drawaione(table)

    #the player plays first
if gamemode == 'interactive':
    if first=='human-next':
        drawhu(table)    
        while validMoves(table):
            n=raw_input("Enter column no. to make your move: ")
            print "Player's move:"
            hmove(table, n)
            drawhu(table)
            move(table, iterDeepening(table), 1)
            print "Player AI Agent's Move:"
            drawai(table)
            
    #The AI agent plays first
    else:
        while validMoves(table):
            move(table, iterDeepening(table), 1)
            print "Player AI Agent's Move:"
            drawai(table)
            n=raw_input("Enter column no. to make your move: ")
            print "Player's move:"
            hmove(table, n)
            drawhu(table)

ag = win(table)
hu = winhu(table)
if ag==hu: print "Score: DRAW"
else: print "Score: Player AI Agent =",ag,", Player =",hu
