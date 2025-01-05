import random

#테스트용
userName='수연'
friends=("은성", "명경", "재훈", "태희")

#아파트 게임
def play_apartment_game(userName: str, friends: tuple):

    print("🏢 아파트 게임에 오신 것을 환영합니다! 🏢")
    print("🏢 아~파트 아파트! 아~파트 아파트! 🏢")
    print(
        f"""
---------____-----________--- _____________-----------------
        /    \    |   __  \  |____     ____|          
       /  __  \   |  |__|  |      |   |  
      /  |__|  \  |   ___ /       |   |
     /  /    \  \ |  |            |   |
----/__/------\__\|__|------------|___|---------------------  
                                                             """)

    #왼손과 오른손
    def apartmentGame_user_hands():
        hands = []
        for player in players:
            hands.append((player, "L"))
            hands.append((player, "R"))
        random.shuffle(hands)
        return hands


    # 게임 참가자 (현재 진행하는 사람 + 함께 취할 친구들) // 테스트용
    players = [userName] + list(friends)

    total_hands = len(players) * 2  
    print(f"\n현재 최대 {total_hands}층까지 쌓을 수 있습니다.")
    
    floors = int(input("몇 층 〰️❗: "))
    while floors > total_hands:
        print(f"\n❌ 최대 {total_hands}층까지만 쌓을 수 있습니다!")
        floors = int(input("다시 쌓을 아파트의 층수를 입력하세요: "))

    hands = apartmentGame_user_hands()
    hands_with_height = []
    for height, hand in enumerate(hands, 1):  
        hands_with_height.append((height, hand[0], hand[1])) 

    hands_with_height.sort()  

    print("\n🏢 아파트 게임 시작! 🏢")

    for floor in range(1, floors + 1):
        current_hand = hands_with_height[floor - 1]
        print(f"층 {floor}: {current_hand[1]}의 {current_hand[2]} 손을 쌓았습니다.")

        if floor == floors:  
            print(f"\n🎉 {current_hand[1]}(이)가 마지막 층({floors}층)을 쌓았습니다!")
            print(f"아 누가누가 술을 마셔🍺 {current_hand[1]}(이)가 술을 마셔🍺 원❗샷❗")
            return current_hand[1]

    print("\n게임 종료! 🎉")


# 게임 실행

if __name__ == "__main__":
    play_apartment_game(userName, friends)


