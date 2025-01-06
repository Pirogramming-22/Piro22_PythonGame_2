##### Functions #####
import random
import time


def printIntro():
    introText1 = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
______  _____ ______  _____           ______ ______  _____  _   _  _   __ _____  _   _  _____ 
| ___ \|_   _|| ___ \|  _  |          |  _  \| ___ \|_   _|| \ | || | / /|_   _|| \ | ||  __ \
| |_/ /  | |  | |_/ /| | | |  ______  | | | || |_/ /  | |  |  \| || |/ /   | |  |  \| || |  \/
|  __/   | |  |    / | | | | |______| | | | ||    /   | |  | . ` ||    \   | |  | . ` || | __ 
| |     _| |_ | |\ \ \ \_/ /          | |/ / | |\ \  _| |_ | |\  || |\  \ _| |_ | |\  || |_\ \
\_|     \___/ \_| \_| \___/           |___/  \_| \_| \___/ \_| \_/\_| \_/ \___/ \_| \_/ \____/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    introText2 = r"""
                |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣| 
                 우주 최강 피로그래밍 22기 2주차 2조가 만든 마시면서 배우는 술게임
                |＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
                (\_/)     (\_(\              ᕱ ᕱ  ||
                ( •͈ᴗ•͈)    („• ֊ •„)         ( ･ω･ ||
                />🍺      O🍺O      　       /　つΦ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    print(introText1)
    time.sleep(1)
    print(introText2)
    go = ""
    while(go != 'y' and go != 'Y'):
        go = input("게임을 진행할까요 ? (y / n) : ")
        if go == 'n' or go == 'N':
            exit(0)
        

def getUserName():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    rtn = input("오늘 거하게 취해볼 당신의 이름은? : ")
    while len(rtn.split()) == 0:
        rtn = input(f"이름이 정말 \"{rtn}\"이라고요? 다시 솔직하게 입력해주세요~~ : ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return rtn

def getUserLife():
    # - input: X
    # -기능: (3)pdf 명세대로 출력
    # - return: 입력받은 주량 (단위: 잔, int)
    while(True):
        try:
            print(f"""
        {'~'*20} 🍺 소주 기준 당신의 주량은?? 🍺 {'~'*20}
        {' '*20} 🍺 1. 소주 반병 ( 2잔 )
        {' '*20} 🍺 2. 소주 반병에서 한병 ( 4잔 )
        {' '*20} 🍺 3. 소주 한병에서 한병 반 ( 6잔 )
        {' '*20} 🍺 4. 소주 한병 반에서 두병 ( 8잔 )
        {' '*20} 🍺 5. 소주 두병 이상 ( 10잔 )
        """)
            alcohol = int(input("당신의 치사량( 주량 )은 얼마만큼인가요?(1 ~ 5 중 입력해주세요) : "))
    # 1 ~ 5 사이의 값이 아닌 것에 대한 예외처리
        except ValueError:
            print("😵‍💫 벌써부터 취하셨나요~~?? 😵‍💫 1 ~ 5 사이의 정수를 입력해주세요")
        else:
            if not (1 <= alcohol<= 5):
                ("설마 소주 반병도 못먹는 술찌는 아니겠죠???🧐🧐 1 ~ 5 사이의 숫자를 입력해주세요!")
            else:
                alcohol *= 2
                print(f"오호 당신의 주량은 {alcohol} 잔 이시군요..!\n")
                break
    return alcohol

def getFriends():
    # - input: X
    # - 기능: (4)친구수 입력받기, pdf 명세대로 주량설정하고 출력, [스코어보드 출력, 게임리스트 출력은 메인에서 구현]
    # - return: 선택된 친구 정보 (dictionary: {name : 남은주량})
    while(True):
        try:
            friendsNum = int(input("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : "))
            print()
        except ValueError:
            print('⚠️'*20)
            print("술 게임에 너무 설레어서 급하게 문자를 입력하신건가요??🤔 1 ~ 3까지의 숫자를 입력해주세요 😎")
            print('⚠️'*20)
            print('\n\n')
        else:
            if friendsNum > 3:
                print('⚠️'*20)
                print("지금은 사회적 거리 두기 기간이라 4인 이상 모임은 금지예요. 😷")
                print('⚠️'*20)
                print('\n\n')
            elif friendsNum <= 0:
                print('⚠️'*20)
                print("안타깝게도 술게임을 혼자할 수는 없어요... 😥")
                print('⚠️'*20)
                print('\n\n')
            else:
                break
    
    # 랜덤으로 게임에 참가할 친구 이름
    friendsName = ["은서", "예진", "연서", "하연", "재훈", "수연", "은성", "태희", "명경"]
    friendsName = [name for name in friendsName if name != userName] # 유저 이름 제외
    
    randomFriends = random.sample(friendsName, friendsNum)

    # 랜덤 주량
    alcohol = random.sample(range(1, 11), friendsNum)
    
    for i in range(friendsNum):
        print(f"오늘 취할 친구는 {randomFriends[i]}입니다! (치사량 : {alcohol[i]})")
    
    selectedFriends = {randomFriends[i]: alcohol[i] for i in range(friendsNum)}

    return selectedFriends

def printScoreboard(players: dict, max_life_dict: dict):
    # - input: {유저이름 : 남은주량} 딕셔너리/ max_life_dict: dict추가함
    # - 기능: (4)pdf대로 지금까지마신거, 치사량까지 남은양 출력
    # - return: X
    print("~"*60)
    for player, remaining_life in players.items():
        max_life = max_life_dict[player]
        drank = max_life - remaining_life
        print(f"{player}은(는) 지금까지 {drank}🍺! 치사량까지 {remaining_life}")
    print("~"*60)

def printGameList():
    # - input: X
    # - 기능: (4)pdf대로 오늘의 술게임 목록 출력
    # - return: X
    print("~~~~~~~~~~~~~~~~~ 🍻 오늘의 Alcohol GAME 🍻~~~~~~~~~~~~~~~~~")
    print("                  🍺 1. 아파트 게임 🏢 ")
    print("                  🍺 2. 두부 게임 🍞 ")
    print("                  🍺 3. 369 게임 3️⃣6️⃣9️⃣ ")
    print("                  🍺 4. 레코드 ver2 🎹 ")
    print("                  🍺 5. 딸기 게임🍓 ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def executeGame(isUserTurn: bool, gameSelectPlayer: str):
    # 미니게임 import
    from ApartGame import play_apartment_game
    from dubu import dubuGame
    from game369 import game_369
    from record_ver2 import record_ver2
    from strawberry import parktaehee_strawberry

    # 게임 넘버
    game_numberlist = {
        1: play_apartment_game,
        2: dubuGame,
        3: game_369,
        4: record_ver2,
        5: parktaehee_strawberry
    }
    
    # - input: isUserTurn = 게임을 선택하는 게 유저인지(true) 컴퓨터인지(false)
    isUserTurn =  (gameSelectPlayer == userName)

    # - input: gameSelectPlayer = 게임 선택한 인물 이름
    # - 기능: 유저차례라면 게임 선택 받기 및 게임 실행. 유저차례 아니면 랜덤으로 게임 선택해서 실행(출력양식 pdf 6번 아래 3개줄 참고)
    # - return: 패배자 이름(str)
    if(isUserTurn):
        while True:
            try:
                selectedGame = int(input(f"{gameSelectPlayer}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? (숫자로 입력해주세요) : "))
                if 1<=selectedGame<=5:
                    break
                else:
                    print("게임은~ 5번까지~ 있어요호~ 다!시!입!력!해~! : ")
            except ValueError:
                print("게임은~ 5번까지~ 있어요호~ 다!시!입!력!해~! (숫자로 입력해주세요) : ")
    else:
        selectedGame = random.randint(1, 5)
        print(f"{gameSelectPlayer}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : {selectedGame} ")
        time.sleep(1)
    print(f"~~~~~~~~~~~~~~~~~~~~~~~\n{gameSelectPlayer}님이 게임선택했읍니다!😁")
    loser = game_numberlist[selectedGame](userName, friends, gameSelectPlayer)
    return loser


def everyoneAlived(players: dict):
    # - input: {유저이름 : 남은주량} 딕셔너리
    # - 기능: 모두가 살아 있는지를 return
    # - return: 모두가 살아 있는지 여부(boolean)
    for player, alcohol in players.items():
        if alcohol <= 0:  
            return False  
    return True  

def printGameOver(dead: str):
    # - input: 최종패배자 이름
    # - 기능: pdf 맞게 출력
    # - return: X
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("______________________________________________________________________________________________________________________")
    print("______________________________________________________________________________________________________________________")
    print(f"""
               ______           ____        __            __   _________          ______      __        __   ________   _______
             _| _____|         /    \      |  |_        _|  | |   ______|       _|      |_   |  |      |  | |   _____| |  ___  |
            |  |    ____      /  __  \     |    |_    _|    | |  |___          |    __    |  |  |      |  | |  |___    | |___|  |
            |  |   |__  |    /  /  \  \    |   _  |__|  _   | |      |        |    |  |    | |  |      |  | |      |   |  ____ /
            |  |      |  |  /  /____\  \   |  | |__  __| |  | |   ___|        |    |__|    | |_ |_    _| _| |   ___|   |  |   | |
            |__ |_____| /  /  /      \  \  |  |   |__|   |  | |  |______       |_        _|    |_ |__| _|   |  |_____  |  |   |  |
               |______/   /__/        \__\ |__|          |__| |_________|        |______|        |____|     |________| |__|   |__|
          
            """)
    print("______________________________________________________________________________________________________________________")
    print(f"{dead}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("                               🍺 다음에 술마시면 또 불러주세요~ 안녕! 🍺")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")








##### MAIN!!! #####

if __name__ == "__main__":
    printIntro()
    userName = getUserName()
    user_life = getUserLife()
    players = {userName: user_life}  # 현재 남은 주량
    max_life_dict = {userName: user_life} # 최대 주량
    friends = getFriends() #예외처리 할 것: 유저와 랜덤선택된 컴퓨터 npc의 이름이 같으면 문제 발생함
    players.update(friends)  # 친구들의 남은 주량 추가
    max_life_dict.update(friends)  # 친구들의 최대 주량 추가
    printScoreboard(players, max_life_dict)
    printGameList()
    dead = ""
    loser = executeGame(True, userName)
    players[loser] = players[loser] - 1
    print("누가술을마셔",loser,"가술을마셔")

    #첫 라운드에서 치사량 도달 시 게임 종료
    if players[loser] <=0 :
        dead=loser
        printGameOver(dead)
        exit(0)

    current_turn_index = 0  # 플레이어 순환을 위한 인덱스
    player_names = list(players.keys())  # 플레이어 이름 리스트

    while(everyoneAlived(players)):
        printGameList()
        
        if input("술게임 진행중 ! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요! : ") == "exit":
            print("지치셨군요... 이제 당신은 잠에 듭니다... 💤")
            exit(0)
        
        current_turn_index = (current_turn_index + 1) % len(player_names)
        current_player = player_names[current_turn_index]
        is_user_turn = (current_player == userName)

        loser = executeGame(is_user_turn, current_player)  # `friends`를 유지해서 전달
        players[loser] = players[loser] - 1
        print("누가술을마셔", loser, "가술을마셔")
        printScoreboard(players, max_life_dict)

        dead = loser

    printGameOver(dead)