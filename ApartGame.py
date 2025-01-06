import random

# 아파트 게임 함수
def play_apartment_game(userName: str, players: dict, gameSelectPlayer: str):
    print("🏢 아파트 게임에 오신 것을 환영합니다! 🏢")
    print("🏢 아~파트 아파트! 아~파트 아파트! 🏢")
    print(
        """
---------____-----________--- _____________-----------------
        /    \    |   __  \  |____     ____|          
       /  __  \   |  |__|  |      |   |  
      /  |__|  \  |   ___ /       |   |
     /  /    \  \ |  |            |   |
----/__/------\__\|__|------------|___|---------------------  
                                                             """
    )

    # 참가자의 손 랜덤으로 섞기
    def apartmentGame_user_hands(selected_players):
        hands = []
        for player in selected_players:
            hands.append((player, "L"))  # 왼손
            hands.append((player, "R"))  # 오른손
        random.shuffle(hands)
        return hands

    # 선택된 플레이어와 친구들만 포함
    selected_players = [userName] + [name for name in players if name != userName]
    total_hands = len(selected_players) * 2  

    # 사용자로부터 층수 입력받기
    while True:
        try:
            floors = int(input(f"🏢 몇 층을 쌓겠습니까? (최대 {total_hands}층 가능): "))
            if 1 <= floors <= total_hands:
                break
            else:
                print(f"❌ 1층 이상 {total_hands}층 이하로 입력해주세요.")
        except ValueError:
            print("❌ 유효한 정수를 입력해주세요.")

    print(f"\n🏢 이번 게임은 {floors}층까지 진행됩니다! 🏢")

    # 손 섞기 및 층별 배정
    hands = apartmentGame_user_hands(selected_players)
    hands_with_height = [
        (height, hand[0], hand[1]) for height, hand in enumerate(hands, 1)
    ]

    print("\n🏢 아파트 게임 시작! 🏢")
    for floor in range(1, floors + 1):
        current_hand = hands_with_height[floor - 1]
        print(f"층 {floor}: {current_hand[1]}의 {current_hand[2]} 손을 쌓았습니다.")

        if floor == floors:  # 마지막 층
            print(f"\n🎉 {current_hand[1]}(이)가 마지막 층({floors}층)을 쌓았습니다!")
            print(f"아 누가누가 술을 마셔🍺 {current_hand[1]}(이)가 술을 마셔🍺 원❗샷❗")
            return current_hand[1]  # 패배자 반환

    print("\n게임 종료! 🎉")
   
