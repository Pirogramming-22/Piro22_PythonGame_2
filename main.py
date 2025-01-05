##### Functions #####

def printIntro():
    # - input: X
    # - 기능: (1)인트로 출력
    # - return: X
    print("인트로~~~~~")
    pass

def getUserName():
    # - input: X
    # -기능: (2)유저명 받아서 리턴
    # - return: 입력받은 유저이름
    print("유저 이름은: 은성")
    return "은성"
    pass

def getUserLife():
    # - input: X
    # -기능: (3)pdf 명세대로 출력
    # - return: 입력받은 주량 (단위: 잔, int)
    print("유저의 주량은: 2")
    return 2
    pass

def getFriends():
    # - input: X
    # - 기능: (4)친구수 입력받기, pdf 명세대로 주량설정하고 출력, [스코어보드 출력, 게임리스트 출력은 메인에서 구현]
    # - return: 선택된 친구 정보 (dictionary: {name : 남은주량})
    print("오늘 취할 친구들은: 은서 예진 연서")
    return {"은서" : 2, "예진" : 8, "연서" : 6}
    pass

def printScoreboard(players: dict):
    # - input: {유저이름 : 남은주량} 딕셔너리
    # - 기능: (4)pdf대로 지금까지마신거, 치사량까지 남은양 출력
    # - return: X
    print("스코어보드~~~~:", players)
    pass

def printGameList():
    # - input: X
    # - 기능: (4)pdf대로 오늘의 술게임 목록 출력
    # - return: X
    print("술게임 목록~~~~")
    pass

def executeGame(isUserTurn: bool, gameSelectPlayer: str):
    # - input: isUserTurn = 게임을 선택하는 게 유저인지(true) 컴퓨터인지(false)
    # - input: gameSelectPlayer = 게임 선택한 인물 이름
    # - 기능: 유저차례라면 게임 선택 받기 및 게임 실행. 유저차례 아니면 랜덤으로 게임 선택해서 실행(출력양식 pdf 6번 아래 3개줄 참고)
    # - return: 패배자 이름(str)
    if(isUserTurn):
        input("게임선택하기~: ")
    else:
        print("선택된 게임: 1")
    print(f"~~~~~\n{gameSelectPlayer}님이 게임선택했읍니다!")
        
    print("게임진행 ... ")
    
    return "은성"
    pass

def everyoneAlived(players: dict):
    # - input: {유저이름 : 남은주량} 딕셔너리
    # - 기능: 모두가 살아 있는지를 return
    # - return: 모두가 살아 있는지 여부(boolean)
    return players["은성"] != 0
    pass


def printGameOver(dead: str):
    # - input: 최종패배자 이름
    # - 기능: pdf 맞게 출력
    # - return: X
    print("게임오버..", dead, "사망 ㅜㅜㅜ")
    pass







##### MAIN!!! #####

if __name__ == "__main__":
    printIntro()
    userName = getUserName()
    players = {userName : getUserLife()}
    players.update(getFriends()) #예외처리 할 것: 유저와 랜덤선택된 컴퓨터 npc의 이름이 같으면 문제 발생함
    printScoreboard(players)
    printGameList()
    dead = ""
    loser = executeGame(True, userName)
    players[loser] = players[loser] - 1
    print("누가술을마셔",loser,"가술을마셔")
    printScoreboard(players)
    while(everyoneAlived(players)):
        printGameList()
        
        if input("술게임 진행중 ! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요! : ") == "exit":
            break
        
        # 여기에 다음 플레이할 사람이 유저인지 컴퓨터일지 정하는 로직 추가
        loser = executeGame(False, "예진")  # 요기: 다음 플레이할 사람이 유저면 True, 컴퓨터면 False를 인자로 전달하도록 고쳐야함
        players[loser] = players[loser] - 1
        print("누가술을마셔",loser,"가술을마셔")
        printScoreboard(players)
        
        dead = loser
        

    printGameOver(dead)