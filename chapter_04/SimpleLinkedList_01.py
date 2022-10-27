## 클래스 및 함수선언 부분
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
    
    # 처음 노드앞에 노드삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # 중간에 있는 노드앞에 노드삽입
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
        
    # 마지막노드뒤에 노드삽입
    node = Node()
    node.data = insertData
    current.link = node
    
# 변수선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

# 메인코드부분
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
    
insertNode('다현', '화사')
printNodes(head)

insertNode('사나', '솔라')
printNodes(head)

insertNode('재남', '문별')
printNodes(head)
    
        
        
    
        