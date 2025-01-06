import random

def parktaehee_strawberry(userName: str, friends: tuple, gameSelectPlayer: str):
    players = [userName] + list(friends)
    player_count = len(players)

    current_turn = 0
    strawberry_count = 1
    increasing = True
    print("""
        ======================================
            _ /—-\              /—-\_
            \ \   \ —  - — —-  /   / /
             \ \   \          /   / /
            /  - - - -\ - - - —/ - ——— \\
          /              ———            \\
        |     ㅁ   ㅁ     ㅁ   ㅁ    ㅁ ㅁ   |
        |     ㅁㅁㅁ ㅁㅁ ㅁㅁㅁㅁ ㅁㅁㅁㅁㅁ    |
        |       ㅁㅁㅁㅁㅁㅁㅁㅁ    ㅁ  ㅁ     |
         \    ㅁ    ㅁ   ㅁ    ㅁㅁㅁㅁ   ㅁ  /
          \      ㅁ  ㅁ    ㅁ ㅁ    ㅁㅁ    /
            \        ㅁㅁㅁㅁㅁㅁㅁ        /
              \        ㅁㅁㅁㅁㅁ       /
                 \        ㅁ ㅁ     /
                    \      ㅁ    /
                       \       /
                          ——-
        ========================================
        """)

    while True:
        player = players[current_turn % player_count]

        if player == userName:
            try:
                user_input = int(input(f"{player}, 딸기를 몇 개 말할 것인가요?: "))
                print(f"{player}: {'딸기' * user_input}")
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요.")
                continue

            if increasing:
                if user_input != strawberry_count:
                    print(f"{player}이(가) 틀렸습니다! 게임을 종료합니다.")
                    return player
                else:
                    strawberry_count += 1
            else:
                if user_input != strawberry_count:
                    print(f"{player}이(가) 틀렸습니다! 게임을 종료합니다.")
                    return player
                else:
                    strawberry_count -= 1
        else:  # 다른 플레이어 차례일 때
            if random.random() < 0.2:
                wrong_count = strawberry_count + random.choice([-2, -1, 1, 2])
                print(f"{player}: {'딸기' * max(1, wrong_count)}")
                print(f"{player}이(가) 틀렸습니다! 게임을 종료합니다.")
                return player
            print(f"{player}: {'딸기' * strawberry_count}")

            if increasing:
                if strawberry_count == 8:
                    increasing = False
                    strawberry_count -= 1
                else:
                    strawberry_count +=1
            else:
                if strawberry_count == 1:
                    increasing = True
                    strawberry_count += 1
                else:
                    strawberry_count -=1


        current_turn += 1