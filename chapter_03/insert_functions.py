# �Լ� ���� �κ�
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("�����͸� ������ ������ ������ϴ�.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
    
# ���� ���� ���� �κ�
katok = []
select = -1           # 1:�߰�  2:����   3:����   4:����