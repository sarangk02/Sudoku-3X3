print("\nSudoku\n")

board = [
    [2,0,9,0,0,0,6,0,0],
    [0,4,0,8,7,0,0,1,2],
    [8,0,0,0,1,9,0,4,0],
    [0,3,0,7,0,0,8,0,1],
    [0,6,5,0,0,8,0,3,0],
    [1,0,0,0,3,0,0,0,7],
    [0,0,0,6,5,0,7,0,9],
    [6,0,4,0,0,0,0,2,0],
    [0,8,0,3,0,1,4,5,0]
]

# Template for sudoku board input 
# board = [
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,],
#     [,,,,,,,,]
# ]    

def printboard():
    print(f"{board[0][0]} : {board[0][1]} : {board[0][2]} | {board[0][3]} : {board[0][4]} : {board[0][5]} | {board[0][6]} : {board[0][7]} : {board[0][8]}")
    print(f"{board[1][0]} : {board[1][1]} : {board[1][2]} | {board[1][3]} : {board[1][4]} : {board[1][5]} | {board[1][6]} : {board[1][7]} : {board[1][8]}")
    print(f"{board[2][0]} : {board[2][1]} : {board[2][2]} | {board[2][3]} : {board[2][4]} : {board[2][5]} | {board[2][6]} : {board[2][7]} : {board[2][8]}")
    print("- - - - - - - - - - - - - - - - -")
    print(f"{board[3][0]} : {board[3][1]} : {board[3][2]} | {board[3][3]} : {board[3][4]} : {board[3][5]} | {board[3][6]} : {board[3][7]} : {board[3][8]}")
    print(f"{board[4][0]} : {board[4][1]} : {board[4][2]} | {board[4][3]} : {board[4][4]} : {board[4][5]} | {board[4][6]} : {board[4][7]} : {board[4][8]}")
    print(f"{board[5][0]} : {board[5][1]} : {board[5][2]} | {board[5][3]} : {board[5][4]} : {board[5][5]} | {board[5][6]} : {board[5][7]} : {board[5][8]}")
    print("- - - - - - - - - - - - - - - - -")
    print(f"{board[6][0]} : {board[6][1]} : {board[6][2]} | {board[6][3]} : {board[6][4]} : {board[6][5]} | {board[6][6]} : {board[6][7]} : {board[6][8]}")
    print(f"{board[7][0]} : {board[7][1]} : {board[7][2]} | {board[7][3]} : {board[7][4]} : {board[7][5]} | {board[7][6]} : {board[7][7]} : {board[7][8]}")
    print(f"{board[8][0]} : {board[8][1]} : {board[8][2]} | {board[8][3]} : {board[8][4]} : {board[8][5]} | {board[8][6]} : {board[8][7]} : {board[8][8]}")

flags = {
    1: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    2: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    3: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    4: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    5: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    6: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    7: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    8: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    },
    9: {
        0:[],
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[]
    }
}


def checkrow(row,num):
    for i in range(9):
        if board[row][i] == num:
            return False
    return True

def checkcol(col,num):
    for i in range(9):
        if board[i][col] == num:
            return False
    return True
               
def checksquare(i,j,num):
    # upper left
    if i in range(0,3) and j in range(0,3):
        for m in range(0,3):
            for n in range(0,3):
                if board[m][n] == num:
                    return False
    
    # upper center
    if i in range(0,3) and j in range(3,6):
        for m in range(0,3):
            for n in range(3,6):
                if board[m][n] == num:
                    return False
    
    # upper right 
    if i in range(0,3) and j in range(6,9):
        for m in range(0,3):
            for n in range(6,9):
                if board[m][n] == num:
                    return False
    
    # middle left
    if i in range(3,6) and j in range(0,3):
        for m in range(3,6):
            for n in range(0,3):
                if board[m][n] == num:
                    return False
    
    # middle center 
    if i in range(3,6) and j in range(3,6):
        for m in range(3,6):
            for n in range(3,6):
                if board[m][n] == num:
                    return False
    
    # middle right 
    if i in range(3,6) and j in range(6,9):
        for m in range(3,6):
            for n in range(6,9):
                if board[m][n] == num:
                    return False
    
    # lower left 
    if i in range(6,9) and j in range(0,3):
        for m in range(6,9):
            for n in range(0,3):
                if board[m][n] == num:
                    return False
    
    # lower center 
    if i in range(6,9) and j in range(3,6):
        for m in range(6,9):
            for n in range(3,6):
                if board[m][n] == num:
                    return False
    
    # lower right 
    if i in range(6,9) and j in range(6,9):
        for m in range(6,9):
            for n in range(6,9):
                if board[m][n] == num:
                    return False
    
    return True

def fillflags(flagdict):
    # selecting number 
    for k in range(1,10):
        # selecting row
        for i in range(9):
            # selecting column
            for j in range(9):
                # checking if number is zero
                if board[i][j] == 0: 
                    # checking row if element already exists
                    if checkrow(i,k):
                    # checking column if element already exists
                        if checkcol(j,k):
                        # checking corresponding square if element already exists
                            if checksquare(i,j,k):
                                # appending column number in row key
                                flagdict[k][i].append(j)

def removeflags(flagdict):
    # selecting number 
    for k in range(1,10):
        # selecting row
        for i in range(9):
            temp = []
            # selecting column
            for j in range(9):
                # checking if number is zero
                if board[i][j] == 0: 
                    # checking row if element already exists
                    if checkrow(i,k):
                    # checking column if element already exists
                        if checkcol(j,k):
                        # checking corresponding square if element already exists
                            if checksquare(i,j,k):
                                # appending column number in row key
                                temp.append(j)
            flagdict[k][i] = temp


def fillnumber(board,flags):
    count = 0
    for a in flags:
        for b in flags[a]:
            x = flags[a][b]
            if len(x) == 1:
                board[b][x[0]] = a
                count += 1
    print('\nTotal numbers filled = ',count)
    # if no number is added then stop the recursion
    if count != 0:
        printboard()
        removeflags(flags)
        fillnumber(board,flags)

print("Initial Board - ")
printboard()
print('\n')

fillflags(flags)

fillnumber(board,flags)


# is the AI getting stucked 
def notSolved():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return True
    return False
if notSolved():
    print("\n\nOops! I can perfectly solve till this stage only, now I have to make a Tukka")
else:
    print("\n\nSudoku solved!!! Cheers...")  


print('\n\n')
print("Final Board - ")
printboard()