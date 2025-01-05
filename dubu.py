###### 두부게임~~~ 김은성이 만듦! ######

import random
import time

    
MO1 = "두부 한 모"
MO2 = "두부 두 모"
MO3 = "두부 세 모"
MO4 = "두부 네 모"
MO5 = "두부 다섯 모"

game_description = f"{MO1} / {MO2} / {MO3} / {MO4} / {MO5} 중 하나를 입력해주세요!"
intro = "두~부두부두부 으쌰으쌰으쌰으쌰! " * 2

def printSeat(players):
    # 원형으로 앉은 모습 출력
    if len(players) == 4:
        state = f"""
        \t\t{players[2]}
        {players[3]}\t\t\t\t{players[1]}
        \t\t{players[0]}
        """   
    elif len(players) == 3:
        state = f"""
        \t{players[2]}\t\t{players[1]}
        
        \t\t{players[0]}
        """    
    elif len(players) == 2:
        state = f"""
        \t\t{players[1]}
        
        \t\t{players[0]}
        """
    
    print(state)
    

def dubuGame(userName: str, friends: tuple):
    ### return : 패자이름: str
    ### 현상황: 시작한사람이 유저인경우만 구현됨.
    print(intro)
    
    players = (userName,) + friends[0:]
    numOfPlayers = len(players)
    printSeat(players)
    
    turn = userName

    
    while (1):
        time.sleep(1)
        if turn == userName:
            print(game_description)
            turn_input = input(userName + ": ")
        else:
            turn_input = random.choice((MO1, MO2, MO3, MO4, MO5))
            print(turn + ": " + turn_input)
            
                
        if turn_input not in ((MO1, MO2, MO3, MO4, MO5)):
            # 잘못된 입력: 패배
            return turn
        
        if turn_input == MO3:
            # 두부 세 모?: 패배
            print("두부는 네모! 두부는 네모! 네모! 네모! 네모네모네모!")
            return turn
        
        if numOfPlayers == 2:
            if turn == players[0]:
                if turn_input == MO2 or turn_input == MO4:
                    turn = players[1]
                else:
                    turn = players[0]
            elif turn == players[1]:
                if turn_input == MO2 or turn_input == MO4:
                    turn = players[0]
                else:
                    turn = players[1]
                    
        elif numOfPlayers == 3:
            if turn == players[0]:
                if turn_input == MO1 or turn_input == MO4:
                    turn = players[1]
                else:
                    turn = players[2]
            elif turn == players[1]:
                if turn_input == MO1 or turn_input == MO4:
                    turn = players[2]
                else:
                    turn = players[0]
            elif turn == players[2]:
                if turn_input == MO1 or turn_input == MO4:
                    turn = players[0]
                else:
                    turn = players[1]
                
                
        elif numOfPlayers == 4:
            if turn == players[0]:
                if turn_input == MO1 or turn_input == MO5:
                    turn = players[2]
                elif turn_input == MO2:
                    turn = players[3]
                elif turn_input == MO4:
                    turn = players[1]
            elif turn == players[1]:
                if turn_input == MO1 or turn_input == MO5:
                    turn = players[3]
                elif turn_input == MO2:
                    turn = players[0]
                elif turn_input == MO4:
                    turn = players[2]
            elif turn == players[2]:
                if turn_input == MO1 or turn_input == MO5:
                    turn = players[0]
                elif turn_input == MO2:
                    turn = players[1]
                elif turn_input == MO4:
                    turn = players[3]
            elif turn == players[3]:
                if turn_input == MO1 or turn_input == MO5:
                    turn = players[1]
                elif turn_input == MO2:
                    turn = players[2]
                elif turn_input == MO4:
                    turn = players[0]
                    
        else:
            turn = userName
                
                
            
        
        
        
        
    
    


# 테스트용
if __name__ == "__main__":
    # dubuGame("p0", ("p1", "p2", "p3"))
    dubuGame("p0", ("p1", "p2"))
    # dubuGame("p0", ("p1",))
