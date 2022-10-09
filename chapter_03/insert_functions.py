# 함수 선언 부분
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
    
# 전역 변수 선언 부분
katok = []
select = -1           # 1:추가  2:삽입   3:삭제   4:종료