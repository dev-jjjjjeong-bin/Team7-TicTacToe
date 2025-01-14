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

def Cpu_move(icon):
    if icon == "O":
        number = 1
    choiceCpu=Cpu_select(board)
    if board[choiceCpu] == " ":
        print('Turn of computer {}'.format(number))
        board[choiceCpu] = icon
    else:
        Cpu_move(icon)

def Cpu_select(board):
    return random.randrange(0,25)
        
def User_move(icon):
    if icon == "X":
        number = 1
    print('Your turn player {}'.format(number))
    choice=int(input('enter your move (1-25)').strip())
    if board[choice-1] == " ": # if user type the same number 
        board[choice-1] = icon
    else:
        print()      
        print( ' That space is taken ')
        
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
def game_start(): 
    print("게임을 시작합니다.")       
    while True: # game loop- running forever
        print_board()
        Cpu_move('O')
        print_board()
        if is_victory("O"):
            print_board()
            print('O Wins! Congratulations!')
            break
        elif is_draw():
            print('its a draw!')
            break
        User_move('X')
        if is_victory("X"):
            print('X Wins! Congratulations!')
            break
        elif is_draw():
            print('its a draw!')
            break