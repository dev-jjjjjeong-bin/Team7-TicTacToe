import tictactoe3x3
import tictactoe3x3AI
import tictactoe5x5
import tictactoe5x5AI

def lobby():
    print("-----------------------")
    print("1. 3X3 TicTaetoe (1 player)")
    print("2. 3X3 TicTaetoe (2 player)")
    print("3. 5X5 TicTaetoe (1 player)")
    print("4. 5X5 TicTaetoe (2 player)")
    print("-----------------------")
    menu = input("선택지를 입력하세요")
    if (menu == "1"):
        #print("1테스트")
        game_explanation1()
    elif (menu == "2"):
        #print("2테스트")
        game_explanation2()
    elif (menu == "3"):
        #print("3테스트")
        game_explanation3()
    elif (menu == "4"):
        #print("4테스트")
        game_explanation4()
    else:
        print("올바르지 않은 입력입니다.")
        lobby()
    
def game_explanation1():
    print("-----------------------")
    print("3X3 TicTaeToe (1 player) 게임 입니다.")
    print("O와 X를 3×3 판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하면 이기는 게임입니다.")
    print("사용자가 한 번 입력하면 컴퓨터가 랜덤으로 한 번 입력합니다.")
    print("게임을 시작하려면 엔터키를 입력하세요.")
    input()
    tictactoe3x3AI.game_start()

def game_explanation2():
    print("-----------------------")
    print("3X3 TicTaetoe (2 player) 게임 입니다.")
    print("O와 X를 3×3 판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하면 이기는 게임입니다.")
    print("두 명의 사용자가 번갈아가며 입력합니다.")
    print("게임을 시작하려면 엔터키를 입력하세요.")
    input()
    tictactoe3x3.game_start()
    
def game_explanation3():
    print("-----------------------")
    print("5X5 TicTaetoe (1 player) 게임 입니다.")
    print("O와 X를 5×5 판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하면 이기는 게임입니다.")
    print("오목과 아주 유사한 게임입니다.")
    print("사용자가 한 번 입력하면 컴퓨터가 랜덤으로 한 번 입력합니다.")
    print("게임을 시작하려면 엔터키를 입력하세요.")
    input()
    tictactoe5x5AI.game_start()
    
def game_explanation4():
    print("-----------------------")
    print("5X5 TicTaetoe (1 player) 게임 입니다.")
    print("O와 X를 5×5 판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하면 이기는 게임입니다.")
    print("오목과 아주 유사한 게임입니다.")
    print("두 명의 사용자가 번갈아가며 입력합니다.")
    print("게임을 시작하려면 엔터키를 입력하세요.")
    input()
    tictactoe5x5.game_start()

lobby() 