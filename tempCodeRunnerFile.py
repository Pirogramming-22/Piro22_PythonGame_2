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

