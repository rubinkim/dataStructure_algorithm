# -*- coding: euc-kr -*-

# 클래스와 함수 선언 부분
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
    
    
# 전역 변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

# 메인 코드 부분
