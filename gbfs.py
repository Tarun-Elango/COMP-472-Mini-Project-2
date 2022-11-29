from vehicle import vehicle
from informedNode import informedNode
import copy
import time
import os.path
import json

# read input file and store data into data structure
def readInput(input):
    valuesArray = []
    folder = './Input'
    name = f"{input}.txt"
    path = os.path.join(folder, name)
    f = open(path,"r")
    for i in f.read().splitlines():
            valuesArray.append(i)

    newArray=[]
    for j in range(len(valuesArray)):
        if(valuesArray[j]=='' or valuesArray[j].startswith('#')):
            continue
        else:
            newArray.append(valuesArray[j])

    return newArray

def printPuzzle(array):
    for i in range(0,len(array)):
        if(i%6==5):
            print(array[i])
        else:
            print(array[i], end =" "),

def printPuzzleTextFile(array, text):
        for i in range(0,len(array)):
            if(i%6==5):
                text.write(array[i])
                text.write('\n')
            else:
                text.write(array[i])
                text.write('')

#create a matrix of the given board
def boardMatrix(input):
    board = [[0]*6 for i in range(6)]
    i=0
    j=0
    k=0
    for q in range(0, len(input)):
        board[i][j] = input[q]
        j = j + 1
        if (q % 6 == 5):
            i = i + 1
            j=0

    return board

def orientation(board,i):
    lt =[]
    for k in range(6):
        for j in range(6):
            if (board[k][j] == f'{i}'):
                lt.append(k)
                lt.append(j)

    if (lt[0] != lt[2]):
        return 'vertical'
    else:
        return 'horizontal'

#get all the car atrributes
def defCar(board, unique):
    cars=[] #hold object os cars
    for i in unique:
        # id, posx, posy, length, ori, fuel
        id = i
        length = sum(length.count(f'{i}') for length in board)
        intermediary = a = [[0]*1]*1
        posx=[]
        posy=[]
        for k in range(6):
            for j in range(6):
                if (board[k][j] == f'{i}'):
                    posx.append(k)
                    posy.append(j)
        orient = orientation(board, i)
        obj = vehicle.setVechicle(i,posx, posy, length, orient)
        cars.append(obj)
    return cars # set of car objects

def computeMove(board, fuel, checkerList, unique): #board has the current nodes board, fuel has the current nodes fuel, checkerList has all the nodes visited
    boards=[]#contains all the boards that have already been passed
    for i in checkerList:
        boards.append(i.board)
    boardList = [] 
    movelist = [] 
    fuelList= [] 
    carlist = defCar(board, unique) #this list has all the cars for the given board

    # give the board, get the car
    #consider boards visited, fuel
    #length 2
    #all left possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
            #for loop 1 to 4, check if for
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    if(j>1):
                        temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[0]][i.posy[0]] = '.'
                            temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[3]][i.posy[3]] = '.'
                    if(j>1):
                        temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==5) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[4]][i.posy[4]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                else:
                    check=True
                

    #all ritgh possible moves 
    for i in carlist:
        if(fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posy[1]+j)<=5 and (board[i.posx[1]][i.posy[1]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[1]][i.posy[1] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posy[2]+j)<=5 and (board[i.posx[2]][i.posy[2]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[2]][i.posy[2] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[2]][i.posy[2]] = '.'
                            temp[i.posx[2]][i.posy[2] + 1] = i.letter
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posy[3]+j)<=5 and (board[i.posx[3]][i.posy[3]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[3]][i.posy[3] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                elif((i.length==5) and (i.posy[4]+j)<=5 and (board[i.posx[4]][i.posy[4]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[4]][i.posy[4] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                else:
                    check=True

    #all up possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] > 0  and i.orientation=='vertical'):
            check=False
            for j in range (1,5):
                if((i.length==2) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    if(j>1):
                        temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[0]][i.posy[0]] = '.'
                            temp[i.posx[0]-1][i.posy[0] ] = i.letter
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                elif((i.length==4) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[3]][i.posy[3]] = '.'
                    if(j>1):
                        temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==5) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[4]][i.posy[4]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                else:
                    check=True

    #all down possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] > 0  and i.orientation=='vertical'):
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posx[1]+j)<=5 and (board[i.posx[1]+j][i.posy[1]]=='.')  and check==False ):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[1]+k][i.posy[1] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posx[2]+j)<=5 and (board[i.posx[2]+j][i.posy[2]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[2]+k][i.posy[2] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[2]][i.posy[2]] = '.'
                            temp[i.posx[2]+1][i.posy[2]] = i.letter
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posx[3]+j)<=5 and (board[i.posx[3]+j][i.posy[3]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[3]+k][i.posy[3] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==5) and (i.posx[4]+j)<=5 and (board[i.posx[4]+j][i.posy[4]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[4]+k][i.posy[4] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                else:
                    check=True

    return boardList, fuelList, movelist

def testcomputeMove(board, fuel, checkerList): #board has the current nodes board, fuel has the current nodes fuel, checkerList has all the nodes visited
    boards=[]#contains all the boards that have already been passed
    for i in checkerList:
        boards.append(i.board)
    boardList = [] 
    movelist = [] 
    fuelList= [] 
    carlist = defCar(board, unique) #this list has all the cars for the given board

    # give the board, get the car
    #consider boards visited, fuel
    #length 2
    #all left possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
            #for loop 1 to 4, check if for
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    if(j>1):
                        temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[0]][i.posy[0]] = '.'
                            temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[3]][i.posy[3]] = '.'
                    if(j>1):
                        temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==5) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[4]][i.posy[4]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel)
                else:
                    check=True
                

    #all ritgh possible moves 
    for i in carlist:
        if(fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posy[1]+j)<=5 and (board[i.posx[1]][i.posy[1]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[1]][i.posy[1] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posy[2]+j)<=5 and (board[i.posx[2]][i.posy[2]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[2]][i.posy[2] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[2]][i.posy[2]] = '.'
                            temp[i.posx[2]][i.posy[2] + 1] = i.letter
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posy[3]+j)<=5 and (board[i.posx[3]][i.posy[3]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[3]][i.posy[3] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel)
                elif((i.length==5) and (i.posy[4]+j)<=5 and (board[i.posx[4]][i.posy[4]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[4]][i.posy[4] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel)
                else:
                    check=True

    #all up possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] > 0  and i.orientation=='vertical'):
            check=False
            for j in range (1,5):
                if((i.length==2) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    if(j>1):
                        temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==3) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[0]][i.posy[0]] = '.'
                            temp[i.posx[0]-1][i.posy[0] ] = i.letter
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel)
                elif((i.length==4) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[3]][i.posy[3]] = '.'
                    if(j>1):
                        temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==5) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[4]][i.posy[4]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                else:
                    check=True

    #all down possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] > 0  and i.orientation=='vertical'):
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posx[1]+j)<=5 and (board[i.posx[1]+j][i.posy[1]]=='.')  and check==False ):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[1]+k][i.posy[1] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posx[2]+j)<=5 and (board[i.posx[2]+j][i.posy[2]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[2]+k][i.posy[2] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[2]][i.posy[2]] = '.'
                            temp[i.posx[2]+1][i.posy[2]] = i.letter
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posx[3]+j)<=5 and (board[i.posx[3]+j][i.posy[3]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[3]+k][i.posy[3] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                elif((i.length==5) and (i.posx[4]+j)<=5 and (board[i.posx[4]+j][i.posy[4]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[4]+k][i.posy[4] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves

                    boardList.append(temp)
                    movelist.append(move)
                    fuelList.append(tempFuel) 
                else:
                    check=True

    return boardList, fuelList, movelist

def h1(board):
    #returns the number of vehicles blocking A to the right 1,2,3
    #blocking vehicles, check row 3, how many car elements present in the row to 'A''s right
    score = []
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            score.append(board[2][i])
    return len(set(score))

def h2(board): # returns the number of alphabets blocking A to the right 
    score = 0
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            score = score + 1
    return score

def h3(board):
    #returns the number of vehicles blocking A to the right 1,2,3
    #blocking vehicles, check row 3, how many car elements present in the row to 'A''s right
    score = []
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            score.append(board[2][i])
    return len(set(score))*5

def h4(board):#combination of how far A is away from [2][5], vehciles blocking a
    veh = []
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            veh.append(board[2][i])
    # A's pos from end
    posFromEnd = 5-posy
    return len(set(veh))*5 + posFromEnd

def valet(board, unique):
    veh = None
    if(board[2][5]!='.' and board[2][4]!='.' and board[2][5]!='A' and board[2][4]!='A'):
        if(board[2][5]==board[2][4]):
            veh = board[2][5]
            #replace 5 and 4 with .
            board[2][5]='.'
            board[2][4]='.'
            unique.remove(veh)
            if(board[2][3]==veh):
                #replace 3 with . 
                board[2][3] = '.'
            if(board[2][2]==veh):
                #replace 3 with . 
                board[2][2] = '.'
    return board

def nextNode(presentNodeValue, checkerList, unique, heuIndex):
    boards, fuels, moves = computeMove(presentNodeValue.board, presentNodeValue.fuel, checkerList, unique)
    newNodes=[]
    # create nodes with the new boards
    for i in range(len(boards)):
        # condition to check if board already visited 
        valetBoard = valet(boards[i], unique)

        obj = informedNode.setinfNode(valetBoard, presentNodeValue, moves[i], int(presentNodeValue.level)+1, fuels[i], h1(boards[i]))# heu = heu 
      
        newNodes.append(obj)

    return newNodes

def gbfs(startBoard, fuel, unique, heuIndex): 

    initial = informedNode.setinfNode(valet(startBoard, unique), None, 'None', 0, fuel, h1(startBoard))

    openList=[] 
    checkerList=[]
    closedList=[]

    openList.append(initial)
    checkerList.append(initial)
    present = openList.pop(0) 
    closedList.append(present)
    while(present.board[2][5] != 'A' ) :
        next_nodes = nextNode(present, checkerList, unique, heuIndex)
        for i in next_nodes:    
            # do the check here
            openList.append(i)
            checkerList.append(i)

        if(len(openList)==0):
            break
        else:
            openList.sort(key=lambda x: x.heu, reverse=False)
            present = openList.pop(0)  
            closedList.append(present)
    searchMoves = []
    searchPath = []

    while(present.previous!=None):
        searchMoves.append(present.move)
        searchPath.append(present.board)
        present = present.previous

    return searchMoves, closedList, searchPath, checkerList

def parseMove(string):
    if string == 'u':
        return '   up'
    if string == 'd':
        return ' down'
    if string == 'l':
        return ' left'
    if string == 'r':
        return 'right'

def solMoveString(searchPathMoves):
    solutionPathString=''
    for i in reversed(searchPathMoves):
        solutionPathString = solutionPathString + i[0]+' '+parseMove(i[1])+' '+i[2]+' ; '
    return solutionPathString

def solPathMoves(searchPathMoves,searchPath):
    for i in reversed(range(len(searchPath))):
        print('{}  {}'.format(searchPathMoves[i][0]+' '+parseMove(searchPathMoves[i][1])+' '+searchPathMoves[i][2]+' ',''.join(map(str,[ i for j in searchPath[i] for i in j]))))

    final = searchPath[0]
    for i in range(6):
        for j in range(6):
                print(final[i][j], end=" ")
        print('')

# function to pretty print solution path to text file
def printSolPathMovesTextFile(searchPathMoves,searchPath, text):
    for i in reversed(range(len(searchPath))):
        text.write('{}  {}'.format(searchPathMoves[i][0]+' '+parseMove(searchPathMoves[i][1])+' '+searchPathMoves[i][2]+' ',''.join(map(str,[ i for j in searchPath[i] for i in j]))))
        text.write('\n')

    text.write('\n')

    final = searchPath[0]
    for i in range(6):
        for j in range(6):
                text.write(final[i][j])
                text.write('')
        text.write('\n')

def printSearchPathTextFile(closedList, i,h):
        #search path result, closedList has all the searched paths
    file = './Output/gbfs/search files'
    fileName = f"gbfs-h{h}-search-{i}.txt"
    pathName = os.path.join(file, fileName)
    searchTextFile = open(pathName,"w+")    

    for p in closedList:
        searchTextFile.write(str(p.heu))
        searchTextFile.write(' ')
        searchTextFile.write(str(p.level))
        searchTextFile.write(' ')
        searchTextFile.write(str(p.heu - p.level))
        searchTextFile.write(' ')
        for k in range(6):
            for j in range(6):
                searchTextFile.write(p.board[k][j])
                searchTextFile.write('')
        searchTextFile.write('\n')

def runChosenPuzzle():
    arrayPuzzle = readInput('input')
    size = len(arrayPuzzle)

    print('number of puzzles ',size)
    check = False
    while(check==False):
        puzzleNumber = input(f'choose puzzle number between 1 and {size} :')
        if (int(puzzleNumber) > int(size) or int(puzzleNumber) < 1):
            print('wrong input')
        else:
            check=True
    unique= sorted(set(arrayPuzzle[int(puzzleNumber)-1][0:36]))
    if '.' in unique: unique.remove('.')
    fuel={}
    for j in range(len(unique)):
        fuel[unique[j]]=100

    remaining = arrayPuzzle[int(puzzleNumber)-1][36:len(arrayPuzzle[int(puzzleNumber)-1])].replace(' ','')
    #print((remaining))
    if(len(arrayPuzzle[int(puzzleNumber)-1])>36):  #integer value should be until the end of file, or before another english.(we remove space)
        check= 0
        while(check<=len(remaining)/2):
            fuel[remaining[check]]=int(remaining[check+1])
            check = check+2
    print(f'initial puzzle is {arrayPuzzle[int(puzzleNumber)-1]}')
    printPuzzle(arrayPuzzle[int(puzzleNumber)-1][0:36])
    print('car fuel available ',fuel)
    start = time.time()
    # following has the board
    board = boardMatrix(arrayPuzzle[int(puzzleNumber)-1][0:36])
    heuChoice = input('enter 1,2,3,4 for the respective heuristic function: ')
    if(int(heuChoice)>4 or int(heuChoice)<1):
        print('invalid choice, default Heuristic 1 will be chosen')
        heuChoice = '1'
    searchPathMoves, closedList, searchPath, allStates = gbfs(board, fuel, unique, heuChoice)
    stop = time.time()
    if(searchPath[0][2][5]!='A'):
        print('no solution')
    else:
        print('solution path ', solMoveString(searchPathMoves))
        print('execution time ',stop-start,' seconds')
        print('search path length',len(allStates), ' states')
        print('solution path length', len(searchPathMoves), ' moves')
        solPathMoves(searchPathMoves, searchPath)

def runAllPuzzle():
    arrayPuzzle = readInput('input') # has all the puzzles
    
    for i in range(1, len(arrayPuzzle)+1):
        for h in (1,5):
            folder = './Output/gbfs/solution files'
            name = f"gbfs-h{h}-sol-{i}.txt"
            path = os.path.join(folder, name)
            textFile = open(path,"w+")
            unique= sorted(set(arrayPuzzle[int(i)-1][0:36]))
            if '.' in unique: unique.remove('.')
            fuel={}
            for j in range(len(unique)):
                fuel[unique[j]]=100
            remaining = arrayPuzzle[int(i)-1][36:len(arrayPuzzle[int(i)-1])].replace(' ','')
            #print((remaining))s
            if(len(arrayPuzzle[int(i)-1])>36):  #integer value should be until the end of file, or before another english.(we remove space)
                check= 0
                while(check<=len(remaining)/2):
                    fuel[remaining[check]]=int(remaining[check+1])
                    check = check+2
            textFile.write(f'initial puzzle is {arrayPuzzle[int(i)-1]}')
            textFile.write('\n\n')
            printPuzzleTextFile(arrayPuzzle[int(i)-1][0:36], textFile)
            textFile.write('\n\n')
            #print('car fuel available ',fuel)
            textFile.write('car fuel available: ')
            textFile.write(json.dumps(fuel))
            textFile.write('\n')
            start = time.time()
            board = boardMatrix(arrayPuzzle[int(i)-1][0:36])
            searchPathMoves, closedList, searchPath, allStates = gbfs(board, fuel, unique, str(h))
            stop = time.time()
            if(searchPath[0][2][5]!='A'):
                textFile.write('no solution')
            else:
                textFile.write('solution path: ')
                textFile.write(solMoveString(searchPathMoves))
                textFile.write('\n')
                textFile.write('execution time : ')
                textFile.write(str(stop-start))
                textFile.write(' seconds')
                textFile.write('\n')
                textFile.write('search path length: ' ) # all the states have been assigned  g(n)
                textFile.write(str(len(allStates)))
                textFile.write(' states')
                textFile.write('\n')
                textFile.write('solution path length: ')
                textFile.write(str(len(searchPathMoves)))
                textFile.write(' moves')
                textFile.write('\n\n')
                printSolPathMovesTextFile(searchPathMoves, searchPath, textFile)
                #solPathMoves(searchPathMoves, searchPath)
            textFile.close()
            printSearchPathTextFile(closedList,i, h)

if __name__ == '__main__':
    optionFlag= False
    while(optionFlag==False):
        runOption = input("Enter 1 to run all puzzle, Enter 2 to exit: ")
        if(runOption=='1'):
            runAllPuzzle()
            runOption=True
        #elif(runOption=='2'):
        ##    runChosenPuzzle()
        #    runOption = True
        elif(runOption=='2'):
            break
        else:
            print('Wrong input, Redo options')
