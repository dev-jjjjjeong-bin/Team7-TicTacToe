import tictactoe3x3
import tictactoe3x3AI
import tictactoe5x5
import tictactoe5x5AI

def lobby():
    print("-----------------------")
    print("틱택토 게임")
    print("1. 게임 모드 선택")
    print("2. 게임 설명")
    print("3. 게임 종료")
    print("-----------------------")
    menu = input("선택지를 입력하세요")
    if (menu == "1"):
        #print("1테스트")
        game_lobby()
    elif (menu == "2"):
        #print("2테스트")
        game_expalnation()
    elif (menu == "3"):
        #print("3테스트")
        quit()
    else:
        print("-----------------------")
        print("올바르지 않은 입력입니다.")
        lobby()
        
def game_lobby():
    print("-----------------------")
    print("1. 3X3 틱택토 (1인)")
    print("2. 3X3 틱택토 (2인)")
    print("3. 5X5 틱택토 (1인)")
    print("4. 5X5 틱택토 (2인)")
    print("-----------------------")
    menu = input("선택지를 입력하세요")
    if (menu == "1"):
        #print("1테스트")
        tictactoe3x3AI.game_start()
    elif (menu == "2"):
        #print("2테스트")
        tictactoe3x3.game_start()
    elif (menu == "3"):
        #print("3테스트")
        tictactoe5x5AI.game_start()
    elif (menu == "4"):
        #print("4테스트")
        tictactoe5x5.game_start()
    else:
        print("올바르지 않은 입력입니다.")
        game_lobby()
    
        
def game_expalnation():
    print("-----------------------")
    print("틱택토 게임은 어쩌고 입니다.")
    print("돌아가려면 엔터키를 입력하세요.")
    input()
    lobby()
        
lobby()



