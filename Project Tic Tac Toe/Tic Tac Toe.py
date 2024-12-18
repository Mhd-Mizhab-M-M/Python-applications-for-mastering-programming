#!/usr/bin/env python
# coding: utf-8

# TIC TAC TOE

# In[1]:


board = [' ' for x in range(10)]


# In[2]:


def boardInput(letter,position):
    board[position]=letter


# In[3]:


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')


# In[4]:


def isSpaceFree(position):
    return board[position] == ' '


# In[5]:


def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True


# In[6]:


def isWinner(letter,board):
    winning_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    
    return any(all(board[i] == letter for i in combo) for combo in winning_combinations)
    
    # return ((b[1] == l and b[2] == l and b[3] == l) or
    # (b[4] == l and b[5] == l and b[6] == l) or
    # (b[7] == l and b[8] == l and b[9] == l) or
    # (b[1] == l and b[4] == l and b[7] == l) or
    # (b[2] == l and b[5] == l and b[8] == l) or
    # (b[3] == l and b[6] == l and b[9] == l) or
    # (b[1] == l and b[5] == l and b[9] == l) or
    # (b[3] == l and b[5] == l and b[7] == l))


# In[7]:


def playerMove():
    flag = True
    while flag :
        pos = int(input("Please select a position to enter the X between 1 to 9"))
        try:
            if pos>0 & pos<10:
                if isSpaceFree(pos):
                    flag = False
                    boardInput('X',pos)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except:
            print('Please type a number')


# In[8]:


def computerMove():
    import random
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = None

    for letter in ['O','X']:
        for i in possibleMoves:
            boardcpy=board[:]
            boardcpy[i]=letter
            if isWinner(letter,boardcpy):
                move=i
                return move

    cornerSpace = []
    for i in possibleMoves:
        if i in [1,3,5,7,9]:
            cornerSpace.append(i)
    if len(cornerSpace)>0:
        move = random.choice(cornerSpace)
        return move

    #Middle Space
    if 5 in possibleMoves:
        move = 5
        return move

    #Edge Space
    edgeSpace = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeSpace.append(i)
    if len(edgeSpace)>0:
        move = random.choice(edgeSpace)
        return move

    # Fallback: Return the first available move if no other move has been set (if move is set to 0)
    # return possibleMoves[0] if possibleMoves else move
# def selectRandom(list):
#     import random
#     ln = len(list)
#     rn = random.randrange(0,ln)
#     return list[rn]


# In[9]:


def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner('O',board)):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, You Loose !")
            break

        if not(isWinner('X',board)):
            move = computerMove()
            if move != None:
                boardInput('O',move)
                print('computer placed an O on position' , move , ':')
                printBoard(board)
            else :
                print("")
        else :
            print("You Win !")
            break
            

    if isBoardFull(board):
        print("Tie game")


# In[ ]:


while True:
    print('--------------------')
    board = [' ' for x in range(10)]
    main()
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break


# In[ ]:




