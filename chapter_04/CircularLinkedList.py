# -*- coding: euc-kr -*-

# Ŭ������ �Լ� ���� �κ�
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    
    if current.link == None:
        return
    print(current.data, end=' ')
    
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()