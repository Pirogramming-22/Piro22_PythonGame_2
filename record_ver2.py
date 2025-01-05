# 1. User에 누가 있는지 받는 함수 => 어차피 call해서 쓸거라 불필요

# 2. 노래 랜덤으로 돌리는 함수
import random
import threading  # input을 3초 동안 받기 위해 사용
import sys
import select
import time
if sys.platform == 'win32':
    import msvcrt  # Windows용 키보드 입력 처리

timeout = 5 # user에게 제한시간을 부여하기 위해 필요(5초)

# input은 (userName: str, friends: tuple)로 정의

def start_game():
    print("""
        ⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⣀⠴⠊⣡⣴⣾⡿⣣⠃⠀⠀
        ⠀⠀⠀⠀⢰⠋⠀⠀⠀⡤⠊⠁⣠⣾⡿⠟⣉⠴⠁⠀⠀⠀
        ⠀⠀⠀⡠⠓⠀⠀⠀⠘⠁⢒⣿⠍⠓⠒⠉⠀⠀⠀⠀⠀⠀
        ⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⡏⠀⠀⠀⠀⠴⠂⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀
        ⢸⠘⠉⠀⠀⠀⣴⣶⢶⢀⠤⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
        ⠀⢷⣿⣵⣴⡆⢙⠉⡘⠟⠉⠁⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀
        ⢀⣾⡉⠣⠵⠶⠎⠉⠀⠀⠀⡠⠖⠛⠉⠉⠉⠙⢦⡀⠀⠀
        ⠀⠊⠑⠂⠀⠤⣄⠀⠀⠀⠀⠀⠀⢀⣠⠄⠒⠀⠘⠁⠀⠀
        ⣴⣒⠤⢤⡠⠔⡏⠀⠀⣀⠀⠀⠀⠀⠈⠙⠒⠢⢴⠑⢢⠀
        ⢸⠘⠉⠀⠀⠀⣴⣶⢶⢀⠤⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
        ⠷⡀⠁⠀⠀⠈⡏⠑⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢠⠁
        ⠀⠈⠉⠉⠉⠉⠱⡀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⡏⠁⠀
        ⠀⠀⠀⠀⠀⠀⢸⠉⠒⠤⠤⢤⡇⠀⠀⠀⠀⢀⢼⣇⠀⠀
        ⠀⠀⠀⠀⠀⢠⠶⠿⠤⠤⠔⠛⡞⠦⣄⡠⡤⢊⣾⠟⠀⠀
        ⠀⠀⠀⠀⠀⢱⣤⣤⣤⠠⢶⡿⠀⠀⠀⠙⠶⠽⠟⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)

def random_track(friends):
    track = random.randint(1, len(friends))
    print(f"{track}번 노래를 선택하셨습니다.")
    return track

# 3. 노래 가사 출력하는 함수
def random_song(track):
    if track == 1:
        print("""
        Golden days are still alive
        외롭다는 말하지 마
        내가 있는 곳, 네가 있을 곳
        The place that I belong
        """)
    elif track == 2:
        print("""
        그냥 쉽게 쉽게 살고 싶은데
        내 하루하루는 왜이리
        놀라울 정도로 어려운건데
        """)
    elif track == 3:
        print("""
        나의 자라나는 마음을
        못 본채 꺾어 버릴 수는 없네
        미련 남길바엔 그리워 아픈 게 나아
        서둘러 안겨본 그 품은 따스할 테니
        """)
    else:
        print("""
        우리의 색은 gray and blue
        엄지손가락으로 말풍선을 띄워
        금새 터질 것 같아 우
        호흡이 가빠져 어지러워
        """)

def get_input(prompt, result):
    print(prompt, end='', flush=True)
    if sys.platform == 'win32':
        # Windows의 경우
        start_time = time.time()
        input_str = ''
        while time.time() - start_time < timeout:
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if char == '\r':  # Enter key
                    print()
                    result.append(input_str)
                    return
                print(char, end='', flush=True)
                input_str += char
            time.sleep(0.1)
    else:
        # Linux/Mac의 경우
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            result.append(sys.stdin.readline().strip())


def print_correct(player):
    print(f"\n\033[1m🌟🌟{player}님 정답입니다!🌟🌟\033[0m\n\n")

# 사람 vs 컴퓨터
# 4. user의 input으로 정답인지 아닌지 확인하는 함수 (user 시작으로 설정)
def random_song_answer_computer(track, userName, playerName, friends):
    friend_id = friends.index(playerName)  # 게임을 시작하는 user index

    answer = ""
    match track:
        case 1:
            answer = "Home Sweet Home"
        case 2:
            answer = "Happy"
        case 3:
            answer = "주저하는 연인들을 위해"
        case 4:
            answer = "Blueming"

    while True:
        if friend_id == len(friends):
            friend_id = 0
        # player가 유저인지 확인
        if friends[friend_id] == userName:
            print('-'*20 + '\n')
            print("⚠️⚠️ 5초 안에 정답을 입력해주세요!! 안그러면 다음 사람에게 차례가 넘어갑니다 ⚠️⚠️\n")
            print('-'*20 + '\n')
            result = []
            input_thread = threading.Thread(target=get_input, args=(f"{friends[friend_id]}님 위 가사에 해당하는 제목을 입력해 주세요!🎶🎶(가사를 다시 보고 싶다면 '가사'를 입력해 주세요)\n\n{userName} : ", result))
            input_thread.daemon = True
            input_thread.start()
            input_thread.join(timeout)

            if not result:  # 시간 초과
                print(f"\n\n⏰ {userName}님 시간 초과! 다음 사람의 차례입니다 ⏰\n")
                friend_id += 1
                continue

            user_input = result[0]
            
            if user_input == "가사":
                random_song(track)
                continue

            user_input = result[0]
        
            if user_input == "가사":
                random_song(track)
                continue
                
            # 여기서부터 정답 체크
            if track == 1:
                if user_input in ["Home Sweet Home", "home sweet home", "홈 스윗 홈", "홈스윗홈"]:
                    print_correct(userName)
                    return userName  # 승자 반환
            elif track == 2:
                if user_input in ["Happy", "happy", "해피"]:
                    print_correct(userName)
                    return userName
            elif track == 3:
                if user_input in ["주저하는 연인들을 위해", "주저하는연인들을위해"]:
                    print_correct(userName)
                    return userName
            else:
                if user_input in ["Blueming", "blueming", "블루밍"]:
                    print_correct(userName)
                    return userName
            
            print("☠️ 틀렸습니다 ㅠㅠ ☠️\n")
            friend_id += 1
        # player가 컴퓨터인지 확인
        else:
            time.sleep(3)
            computer_answer_list = ['음,,,,🤔', '어???!!!!🫨', '너무 빨라요 ㅠㅠㅠ😭', '아 뭔지 알 것 같은데🤨', '아니 이게 뭐야??🥶']
            computer_answer_list.append(answer) # 컴퓨터 정답 리스트에 추가

            computer_answer = random.choice(computer_answer_list)

            print(f"{friends[friend_id]} : {computer_answer}\n")
            if computer_answer == answer:
                print_correct(friends[friend_id])
                return friends[friend_id]  # 컴퓨터가 이겼을 때만 게임 종료
            else:
                print("☠️ 틀렸습니다 ㅠㅠ ☠️\n")
                friend_id += 1  # 다음 플레이어로 넘어감

# 리턴값은 패자 이름(str) 리턴
def end_game(playerName, friends):
    print("🎶🎶게임이 종료되었습니다!🎶🎶")
    print(f"🍻{playerName}님 제외 전원 한잔~🍻\n")
    drink_list = tuple(x for x in friends if x != playerName)
    # 패자 이름 출력(winner 제외)
    return drink_list

# userName: 키보드를 입력하는 사람 / playerName: 게임을 시작한 사람 / friends: 게임에 참여한 사람
def record_ver2(userName, playerName, friends):
    start_game()
    print(f"{playerName}님 게임을 시작합니다!")
    print(f"참여자는 {friends}입니다.")
    track = random_track(friends)
    random_song(track)
    winner = random_song_answer_computer(track, userName, playerName, friends)
    end_game(winner, friends)