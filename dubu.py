###### 두부게임~~~ 김은성이 만듦! ######

import random
import time

    
MO1 = "두부 한 모"
MO2 = "두부 두 모"
MO3 = "두부 세 모"
MO4 = "두부 네 모"
MO5 = "두부 다섯 모"

game_intro_art = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
⢯⡳⡽⣕⢯⢞⡵⣫⢞⡵⣫⢞⡵⡳⣝⢮⡳⣝⢮⡳⡵⣝⢮⡳⣕⢗⣝⢮⡫⡳⣝⢮⡺⣪⡳⣕⢗⢽⡱⣝⢮⡺⣪⢳⢝⣎⢯⡳⡝⣎⢗⡝⡮⣪⢳⢕⢧⢳⡹⡜⡮⣪⢳⡹⣪⢣⡳⡹⣪⢣⡫⡺⡜⣎⢮⢺⡸⣪⢺⡸⣪⢣⡳⡹⣜⢮
⢵⡫⡯⣺⢝⡵⣫⢞⡵⣫⢞⡵⡽⣝⢮⡳⣝⢮⡳⣝⢞⢮⡳⣝⢮⡳⣕⢗⢽⡹⣪⡳⣝⢮⡺⣪⢳⡳⣝⢮⡳⣝⣮⣳⣳⣵⣷⣳⣽⣞⣷⣻⣾⢮⣳⡹⣪⡣⣳⢹⡪⣎⢞⡜⣎⢧⢳⡹⡜⡵⡹⡜⡮⣺⢸⢕⡕⡧⡳⣕⢕⢧⡫⡺⣜⢮
⣗⢯⢯⣺⢵⡫⣗⡽⣺⢕⡯⣞⢽⡪⣗⢽⡪⣗⣝⢮⣫⡳⣝⢮⡳⣝⢮⣫⢳⢝⢮⡺⣪⡳⣝⢮⢳⡹⣺⣯⣿⣿⣽⣟⡿⣯⣿⣽⢿⣻⣟⣯⣿⣻⣽⣾⢮⣺⢜⢮⢺⢜⢮⢺⢜⡎⡧⣳⢹⡪⣳⢹⡪⡎⣗⢵⢹⡪⡇⣗⢝⢵⡹⡕⣗⢕
⢯⢯⣳⡳⡽⣺⢵⣫⢞⡽⣪⢷⢝⡮⣳⣝⢮⡳⣕⣗⢵⢝⡮⣳⢝⡮⣳⢕⡯⣫⡳⣝⢮⡺⣜⡕⣗⢝⡽⣯⣿⣾⡿⣯⣿⢿⣽⣾⣿⣯⣿⣷⢷⡯⡿⡾⣟⣯⡿⣮⣳⢹⡪⡳⣕⢽⡸⣪⡣⣏⢮⢣⡳⡹⡜⣎⢧⢳⡹⣜⢕⢧⢳⢝⡎⡧
⡯⣳⡳⡽⣝⢮⢗⣗⡽⣝⢮⢯⡳⡽⣕⣗⢽⡪⣗⢵⡫⣗⢽⡪⣗⢽⡪⣗⢽⡺⣺⣪⡳⣝⢮⡺⣪⡳⣝⣞⣟⣿⣿⣿⡿⣿⡿⣯⣿⣯⣿⣾⢿⣻⣟⣯⣿⢿⣽⢿⣾⢵⡹⣪⢺⢜⢮⢪⡺⡸⣪⡣⣏⢮⡣⡳⡕⡧⡳⡕⣝⢎⡗⡵⡹⡜
⡯⣳⢽⢝⡮⡯⣳⡳⣝⢮⢯⡳⡽⣝⢮⡺⣕⢯⢞⡵⣫⢞⡵⣫⢞⡵⣫⢞⡵⣫⢞⡮⣺⢕⢷⢝⡞⣞⣞⣞⢮⢷⣻⣷⣿⡿⣿⡿⣯⣿⣯⣿⣿⣿⢿⣽⣾⣿⡿⣟⣿⡿⣜⢎⡗⣝⢎⢧⡫⡺⡜⡮⡺⡜⣎⢗⡝⣎⢗⢽⡸⡕⡧⡫⡎⣗
⣞⢽⣕⢯⣞⢽⣺⡪⣗⢯⡳⡽⣝⢮⡳⡽⣺⢝⣵⡫⣗⢯⡫⣞⡵⣫⢞⡽⣪⢯⡳⣝⢮⢏⢷⢝⢮⣳⣳⡳⣫⢯⣞⣿⣽⣿⣿⣿⣿⢿⣯⣿⣿⣾⣿⣿⣿⣽⣿⣿⣿⣿⢎⢧⡫⣎⢗⢵⡹⣪⢳⡹⣪⢳⢕⢧⢫⢎⢗⡕⣇⢯⢪⢇⢯⢪
⢾⢕⡷⣝⢮⣳⡳⣝⢮⢗⡽⣝⢮⡳⡽⣝⢮⢯⡺⣪⢗⡽⣪⢗⡽⣪⢯⡺⣕⣗⣝⢮⡳⣝⢵⡫⡳⡵⣷⣝⢮⣳⡳⣯⣿⣷⣿⣷⣿⣿⣿⣿⢿⣿⣿⣻⣽⣿⣿⡿⣟⣿⣝⢮⢺⢜⡕⣇⢯⡪⡇⡯⣺⢸⢕⡝⣎⢗⢵⢹⢜⢎⢧⢫⢎⢧
⢽⣕⢯⢞⣗⢗⡽⣪⢯⡳⡽⣪⢷⢝⡽⣪⢯⡳⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⡺⡼⡵⣝⢮⡳⣝⢽⣺⣳⢯⣗⣗⡽⣽⣻⣯⣷⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢹⡪⣇⢯⢺⡸⣪⢳⡹⡜⣎⢧⢳⡱⡝⣜⢵⢹⢜⢕⢇⡏⡮
⡽⣪⢯⣳⡳⣝⣞⢵⣫⢞⡽⣪⢗⡯⣺⢕⡯⣺⢕⢯⡺⣕⢯⡺⣪⡳⣝⢮⡳⣝⢮⡳⣕⢗⣝⢮⣳⡳⡽⣝⣞⢞⣞⢞⡮⡿⣿⣿⣯⣿⣿⣻⣿⣿⣻⣿⣿⣿⢿⣿⣿⣿⢎⢧⢳⡱⣣⢳⡱⡕⣇⢗⡝⣜⢎⢧⢳⡹⡜⣎⢇⢯⢪⡣⣣⢫
⣺⡳⣝⢮⡺⣕⣗⢽⡪⣗⢽⡪⣗⣝⢮⡳⣝⢮⣫⡳⣝⢮⡳⣝⢮⡺⣪⡳⣝⢮⡳⡝⡜⡕⡕⡝⣾⢾⢽⣕⢷⢝⣮⣻⣺⣻⢯⣿⣻⣻⣿⣿⣟⣿⣿⡿⣿⣾⣿⣿⣷⣿⣳⢹⢜⢎⢮⡪⡺⡜⣎⢮⢺⡸⣪⢣⡳⡱⡝⡜⡎⣇⢧⢣⡣⡳
⣗⢽⡪⣗⢽⡺⣪⡳⣝⢮⡳⣝⢮⢮⡳⣝⢮⡳⡵⣝⢮⡳⣝⢮⡳⣝⢮⡺⡪⡳⡱⡱⡱⡱⡱⡹⡸⣫⢷⣳⢯⡻⡮⣞⣞⣞⣟⣞⡮⣷⣻⣾⣿⣿⣿⣿⣿⢿⣿⢿⣟⣿⣮⡳⡹⣪⢣⡫⡺⡜⣎⢮⢣⡳⡱⣣⢳⡹⣸⢱⡹⡸⡜⣜⢜⢎
⢾⢕⡯⣺⢕⡯⣺⣪⡳⡳⣝⢮⡳⡳⣝⢮⡳⣝⢞⢮⡳⣝⢮⡳⣝⢮⢣⢣⢣⢣⢣⢣⢣⢣⢣⢣⢣⢪⢪⢺⡽⣽⢽⣳⣳⣳⣳⣳⢽⢮⡷⣿⣽⣿⣯⣿⣾⣿⣿⣿⢿⡿⣞⡮⡫⡎⣇⢯⢺⢜⢎⢮⢣⡳⡹⡜⡼⡸⡜⣜⢜⢎⢮⢪⡪⡣
⣝⢵⡫⣞⢵⣫⡺⣜⢮⡫⡮⡳⣝⢝⢮⡳⣝⢮⡫⡳⣝⢮⡳⣝⢮⡣⡣⡣⡣⡣⡣⡣⡣⡇⡇⢇⢕⢕⢕⢕⢽⣺⡽⣞⣗⣟⡾⡽⣯⡿⣿⢿⣻⣿⣿⣿⣿⣿⢿⣻⣿⣿⣟⢮⡳⡹⣜⢎⢧⡫⣎⢧⢳⡱⡝⣜⢎⢧⢫⢎⢮⢣⡳⡱⡕⣝
⡮⡳⣝⢮⡳⡵⣝⢮⡳⣝⢮⡫⡮⣫⡳⣝⢮⡳⣝⢕⡗⡵⣝⢮⡣⡣⡣⣣⡳⣳⢵⡱⣕⢕⢕⢕⢕⢕⢕⢕⣯⡷⡿⣽⣞⣗⡯⡿⣽⣻⢻⢫⢯⣷⡿⣟⣷⣿⣿⣿⣿⣷⣿⢣⡫⣺⢸⢕⢇⡗⣕⢧⢳⢕⢽⢸⡪⣣⢳⡹⡸⡱⡕⣝⢜⢎
⣝⡝⡮⡳⣝⢮⢮⡳⣝⢮⡳⣝⢮⡺⣜⢮⡳⣝⢮⡳⣝⢞⢼⢕⢵⢱⡱⡱⡝⣎⢮⡺⣜⢮⢳⡹⡜⡜⣾⣻⡯⣟⣯⣷⣻⣺⢽⢽⢺⢸⢸⢸⢹⡪⡟⣟⢯⢗⢟⢮⢷⡿⡮⣣⢫⢎⢮⢣⡳⡱⡕⣇⢗⢝⡜⣕⢕⡕⣕⢕⢝⢜⡜⣜⢜⢜
⡺⡪⣏⢯⢎⣗⢧⡫⡮⡳⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢕⢕⢧⢳⡹⡪⣪⡺⣜⢮⢳⢕⣇⢯⢮⡪⣞⢟⡯⣳⢳⣫⢯⢫⢣⢣⢣⢣⠱⡑⡕⡕⡕⢕⠕⢕⢕⢕⢝⢜⢜⢎⢧⢳⡱⡕⣝⢜⢎⢮⢣⢇⢧⢣⡣⡣⡳⡹⡸⡸⡸⡸⡱
⢯⡫⡮⣳⢳⢕⣗⢝⢮⡫⡮⡳⣝⢮⡳⣝⢮⡳⣝⢮⡳⣝⢮⢞⣌⢇⢗⢵⢝⢮⢺⢜⡎⡇⡇⡗⡝⡜⣜⢜⢵⢹⢸⢱⢱⢱⢱⢱⢑⢕⢕⢕⢕⢌⠪⡪⠢⡣⡑⢕⢕⢕⢕⢕⢕⢕⢇⢗⢝⡜⡎⣇⢗⢕⢵⢱⢕⢕⢝⢜⢜⢎⢎⢇⢇⢧
⡳⣝⢞⢮⡳⡳⣕⢯⡳⣝⢮⡫⡮⡳⣝⢮⡳⣝⢮⡳⡝⣎⣗⣟⡮⣗⡯⣯⡳⣹⢪⢣⢣⡣⡣⡫⡪⡪⡪⣪⢣⢣⢣⢣⢣⢣⢣⢣⠱⡑⢕⢕⢕⢕⢕⢜⢜⢌⠪⡢⡑⢕⢕⢕⢕⢕⢕⢝⢜⡜⡎⣎⢎⢇⢧⢣⢣⢳⢱⢱⢕⢕⢕⢕⢕⢕
⣫⢮⡳⡳⣝⢞⢮⡳⣝⢮⡳⣝⢮⡫⣎⢗⡝⡮⡣⣏⢞⢮⣞⣞⢮⢗⣟⣞⢎⢎⢎⡎⡇⡇⡇⡏⡎⡎⡎⡎⡎⡎⡎⡎⡎⡎⡆⡣⡣⡱⡑⢕⢕⢕⢕⢕⢕⢕⢕⢜⢜⢔⢕⢅⢕⢔⢕⢕⢕⡕⡵⡱⡕⡵⡱⡱⡕⡕⣕⢕⢕⢕⢝⢜⢕⢕
⡮⡳⣝⢞⢮⡳⡣⡯⣪⡳⣝⢮⡳⣝⢮⡳⣝⢎⢯⡪⡫⣗⡷⡽⣝⣗⣗⣗⣕⢇⢧⢣⢫⢪⢪⢪⠪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡢⡑⡕⢕⢕⢕⢕⢕⢕⢅⢕⢔⢕⢕⢕⢕⢕⢕⢕⢕⢵⢱⢕⢕⢵⢱⢱⢱⢱⢱⢕⢕⢕⢕⢕
⡺⣝⢮⡳⣳⡹⡵⣝⢮⡺⣪⢳⢝⢮⡳⣝⢮⢳⡣⡣⣫⣗⣯⣻⣺⣺⣺⣺⡺⡜⡎⡎⡇⡇⡇⡇⡣⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡢⡑⢕⢔⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢝⢜⢜⢜⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕⢕
⣝⢮⡳⣝⢮⣪⡳⣕⢗⣝⢮⡳⣝⢮⡺⣜⢮⡳⡱⣑⢗⣗⣗⣗⣗⣗⣗⢷⢝⢎⢮⢪⢪⠪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⣪⣎⢎⢎⠪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡢⡣⡱⡱⡱⡱⡱⡱⡱⡱⡱⡱⡹⡸⡸⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪⡪
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"나야, 두부" 두부게임 시작~!
'''
game_description = f"{MO1} / {MO2} / {MO3} / {MO4} / {MO5} 중 하나를 입력해주세요!"
intro = "두~부두부두부 으쌰으쌰으쌰으쌰❗" * 2

def printSeat(players):
    # 원형으로 앉은 모습 출력
    print("현재 자리 배치는 다음과 같습니다.")
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
    

def dubuGame(userName: str, friends: tuple, gameSelectPlayer: str):
    ### return : 패자이름: str
    ### 수정: 시작한사람이 유저인경우만 구현됨. -> 시작한 사람이 컴퓨터일 때도 구현함. + 종료시 출력 추가
    print(game_intro_art)
    time.sleep(1)
    
    players = (userName,) + friends[0:]
    numOfPlayers = len(players)
    
    printSeat(players)
    
    time.sleep(1)
    print(intro + '\n')
    
    turn = gameSelectPlayer

    
    while (1):
        time.sleep(1)
        if turn == userName:
            print(game_description)
            turn_input = input(userName + ": ")
        else:
            turn_input = random.choice((MO1, MO2, MO3, MO4, MO5))
            print(turn + ": " + turn_input)
            
        time.sleep(0.5)
        if turn_input not in ((MO1, MO2, MO3, MO4, MO5)):
            # 잘못된 입력: 패배
            print("저런.. 집중력이 떨어지셨군요? 입력을 정확히 하셨어야 했을텐데... 벌써 취하신 건 아니겠죠?")
            time.sleep(0.5)
            print(f"아 누가누가 술을 마셔🍺 {turn}(이)가 술을 마셔🍺 원❗샷❗")
            return turn
        
        if turn_input == MO3:
            # 두부 세모?: 패배
            print("두부는 네모! 두부는 네모! 네모! 네모! 네모네모네모!")
            time.sleep(0.5)
            print(f"아 누가누가 술을 마셔🍺 {turn}(이)가 술을 마셔🍺 원❗샷❗")
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
    dubuGame("p0", ("p1", "p2", "p3"), "p2")
    # dubuGame("p0", ("p1", "p2"), "p1")
    # dubuGame("p0", ("p1",))
