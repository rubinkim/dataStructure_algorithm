# ??? ???? ?��?
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
    
    
# ???? ???? ???? ?��?
katok = []
select = -1           # 1:???  2:????   3:????   4:????


# ???? ??? ?��?
if __name__ == "__main__":
    
    while(select != 4):
        select = int(input("Choose(1:add 2:insert 3:delete 4:quit) -->"))
        
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