## Ŭ���� �� �Լ����� �κ�
from email import header
from os import pread
from platform import node


class Node:
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    
    if current == None:
        return
    print(current.data, end=' ')
    
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()
    
def insertNode(findData, insertData):
    global memory, head, current, pread
    
    # ó�� ���տ� ������
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # �߰��� �ִ� ���տ� ������
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    # ���������ڿ� ������
    node = Node()
    node.data = insertData
    current.link = node
    
# �������� �κ�

        
        
    
        