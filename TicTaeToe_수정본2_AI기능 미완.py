import random

board =[" "for i in range(25)]

def print_board():
    row1 = '|{}|{}|{}|{}|{}|'.format(board[0],board[1],board[2],board[3],board[4]) 
    row2 = '|{}|{}|{}|{}|{}|'.format(board[5],board[6],board[7],board[8],board[9])  
    row3 = '|{}|{}|{}|{}|{}|'.format(board[10],board[11],board[12],board[13],board[14]) 
    row4 = '|{}|{}|{}|{}|{}|'.format(board[15],board[16],board[17],board[18],board[19]) 
    row5 = '|{}|{}|{}|{}|{}|'.format(board[20],board[21],board[22],board[23],board[24]) 

    print()
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print()

#def player_move(icon):
#    if icon == "X":
#        number = 1
#    elif icon == 'O':
#        number = 2
#    print('Your turn player {}'.format(number))
#    
#    choice=int(input('enter your move (1-25)').strip())
#    if board[choice-1] == " ": # if user type the same number 
#        board[choice-1] = icon
#    else:
#        print()      
#        print( ' That space is taken ')

def User_move(icon):

    print("Your turn to move player")
    choice = int(input("Enter your move (1-25)").strip())

#choice=int(input('enter your move (1-25)').strip())
    if board[choice-1] == " ": # if user type the same number 
        board[choice-1] = icon
    else:
        print()      
        print( ' That space is taken ')
        choice = User_move(board)
    return int(choice)

def Board_update(board, index, letter):
    board[index] = letter

def Blank(board, index):
    return board[index] == " "

def Board_copy(board):
    lst = []
    for i in board:
        lst.append(i)
    return lst

def Cpu_move(board):
    for i in range(0, 24):
        
        copy = Board_copy(board)
        
        if Blank(copy, i):
            Board_update(copy, i, 'X')
            
            if is_victory(copy, 'X'):
                return i
            
    for i in range(0, 24):
        
        copy = Board_copy(board)
        
        if Blank(copy, i):
            Board_update(copy, i, 'O')
    
            if is_victory(copy, 'O'): 
                return i
            
    point = Cpu_moveRandom(board, [0,2,4,6,8,10,12,14,16,18,20,22,24])
    
    if point != None:
        return point
    
    elif board[12] == ' ':
        return 12

    return Cpu_moveRandom(board, [1,3,5,7,9,11,13,15,17,19,21,23])
    

def Cpu_moveRandom(board, info):
    lst = []
    for i in info:
        if Blank(board,i):
            lst.append(i)
    if len(lst) > 0:
        return random.choice(lst)
    else:
        return None
        
def is_victory(icon):        
    if(board[0]== icon and board[1]==icon and board[2]==icon and board[3]==icon and board[4]==icon) or\
      (board[5]== icon and board[6]==icon and board[7]==icon and board[8]==icon and board[9]==icon) or\
      (board[10]== icon and board[11]==icon and board[12]==icon and board[13]==icon and board[14]==icon) or\
      (board[15]== icon and board[16]==icon and board[17]==icon and board[18]==icon and board[19]==icon) or\
      (board[20]== icon and board[21]==icon and board[22]==icon and board[23]==icon and board[24]==icon) or\
      (board[0]== icon and board[5]==icon and board[10]==icon and board[15]==icon and board[20]==icon) or\
      (board[1]== icon and board[6]==icon and board[11]==icon and board[16]==icon and board[21]==icon) or\
      (board[2]== icon and board[7]==icon and board[12]==icon and board[17]==icon and board[22]==icon) or\
      (board[3]== icon and board[8]==icon and board[13]==icon and board[18]==icon and board[23]==icon) or\
      (board[4]== icon and board[9]==icon and board[14]==icon and board[19]==icon and board[24]==icon) or\
      (board[0]== icon and board[6]==icon and board[12]==icon and board[18]==icon and board[24]==icon) or\
      (board[4]== icon and board[8]==icon and board[12]==icon and board[16]==icon and board[20]==icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

while True: # game loop- running forever
    print_board()
    User_move('X')
    print_board()
    if is_victory("X"):
        print('Player Wins! Congratulations!')
        break
    elif is_draw():
        print('its a draw!')
        break
    Cpu_move('O')
    if is_victory("O"):
        print_board()
        print('CPU Wins! Congratulations!')
        break
    elif is_draw():
        print('its a draw!')
        break