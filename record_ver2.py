# 1. User에 누가 있는지 받는 함수 => 어차피 call해서 쓸거라 불필요
# def user_input(user_list):

# 2. 노래 랜덤으로 돌리는 함수
import random

def random_track(user_list):
    track = random.randint(1,len(user_list))
    return track

# 노래 목록
    
# 3. 노래 가사 출력하는 함수
def random_song(track):
    if track == 1:
        print("""
        Golden days are still alive
        외롭다는 말하지 마
        내가 있는 곳, 네가 있을 곳
        The place that I belong""")
    elif track == 2:
        print("""
        그냥 쉽게 쉽게 살고 싶은데
        내 하루하루는 왜이리
        놀라울 정도로 어려운건데""")
    elif track == 3:
        print("""
        나의 자라나는 마음을
        못 본채 꺾어 버릴 수는 없네
        미련 남길바엔 그리워 아픈 게 나아
        서둘러 안겨본 그 품은 따스할 테니\n""")
    else:
        print("""
        우리의 색은 gray and blue
        엄지손가락으로 말풍선을 띄워
        금새 터질 것 같아 우
        호흡이 가빠져 어지러워
        """)
        
# 4. user의 input으로 정답인지 아닌지 확인하는 함수
def random_song_answer(track):
    user_input = input("해당 가사에 해당하는 정답을 입력해 주세요!!!")

# 5. 정답이라면 End, 틀렷다면 다른 User가 Input을 넣을 수 있도록 설정