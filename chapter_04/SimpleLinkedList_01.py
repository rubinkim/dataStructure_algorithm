# -*- coding: euc-kr -*-
## Ŭ���� �� �Լ����� �κ�
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
memory = []
head, current, pre = None, None, None
dataArray = ['����','����','����','�糪','��ȿ']

# �����ڵ�κ�
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)
    
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
        
    printNodes(head)
    
insertNode('����', 'ȭ��')
printNodes(head)

insertNode('�糪', '�ֶ�')
printNodes(head)

insertNode('�糲', '����')
printNodes(head)
    
        
        
    
        