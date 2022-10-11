## 함수 선언 부분 ##
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("you are out of range.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
def delete_data(position):
    if position < 0 or position > len(katok):
        print("you are out of range.")
        return
    
    kLen = len(katok)
    katok[position] = None
    
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
        
    del katok[kLen-1]
    
    
## 전역 변수 선언 부분 ##
katok = []
select = -1           # 1:???  2:????   3:????   4:????


## 메인 코드 부분 ##
if __name__ == "__main__":
    
    while(select != 4):
        select = int(input("선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료) -->"))
        
        if(select == 1):
            data = input("data to add-->")
            add_data(data)
            print(katok)
            
        elif(select == 2):
            pos = int(input("position to insert-->"))
            data = input("data to insert-->")
            insert_data(pos, data)
            print(katok)
            
        elif(select == 3):
            pos = int(input("position to delete-->"))
            delete_data(pos)
            print(katok)
            
        elif(select == 4):
            print(katok)
            exit
        
        else:
            print("Choose one from 1 to 4.")
            continue