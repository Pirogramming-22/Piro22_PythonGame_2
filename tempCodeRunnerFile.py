def game_369(userName: str, friends: tuple, gameSelectPlayer: str):
    # 369 오프닝

    def intro_369():
        print(
           f"""
----------------------------------------------------------------------------------
______   ____ ______
|____ | / ___||  _  |
    / // /___ | |_| |
    \\ \\|  __ \\\\___ |
.___/ /| \\_/ |.___/ |
\\____/ \\_____\\/____/ 
----------------------------------------------------------------------------------
번갈아가며 숫자를 외치며, 숫자에 '3', '6', '9'가 포함되면 포함된 개수만큼 X를 외쳐주세요!
{userName} 부터 시작이에요~🍺
        """
    )

        time.sleep(1)
        print("🍾3~69 369!! 3~69 369!!🍾🎉")
        time.sleep(1)


    #게임 규칙 체크
    def check_369(number, choice):
        count_clap = str(number).count('3') + str(number).count('6') + str(number).count('9')
        if count_clap > 0:
            return choice == 'X'*count_clap
        else:
            return choice == str(number)

    #players 정의
    players = []
    players.append(userName)
    for friend in friends:
        players.append(friend)

    #오프닝 실행
    intro_369()

    #게임진행
    turn = 0
    number = 1
    while True:
        current_player = players[turn%len(players)]
        count_clap = str(number).count('3') + str(number).count('6') + str(number).count('9')

        #사용자 turn
        if current_player==userName:
            choice = input(f"{userName}: ")
        #컴퓨터 turn
        else:
            if count_clap > 0:
                 choice = 'X'*count_clap
            else:
                choice = str(number)
            print(f"-{current_player}:{choice} ")
            time.sleep(0.3)

        # 입력 검증
        if not check_369(number, choice):
            print(f"\n아 누가누가 술을 마셔 {current_player}이(가) 술을 마셔 원~~~샷!")
            return current_player
        
        # 차례 업데이트
        turn +=1
        number +=1


# 테스트 실행
if __name__ == "__main__":
    game_369("p0", ("p1", "p2", "p3"), "p2")