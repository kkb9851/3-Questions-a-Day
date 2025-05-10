# 큐(Queue): 한쪽에서 자료를 넣고 다른 쪽에서 꺼내는 구조
# front, rear의 포인터를 통해 구현
# 큐 예제: 요세푸스 순열


# 큐 기본 연산 (queue 모듈 활용)
from queue import Queue
q = Queue()
q.put(data)    # push
q.get()        # pop


# 요세푸스 순열
from collections import deque

def josephus(n, k):
    q = deque(range(1, n + 1))
    result = []
    while q:
        q.rotate(-(k - 1))
        result.append(q.popleft())
    return result


# 클래스 기반의 큐 구현
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def insert(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node   # 현재 큐 객체의 tail에 새로운 노드 추가
        self.tail = new_node        # tail 재설정.

    def popleft(self): 
        if self.is_empty():
            print("empty queue")
        new_node = self.head.next
        delete_node = self.head
        self.head = new_node
        return delete_node.value

    def top(self):
        if not self.is_empty():
            return self.head.value
        else:
            print("empty queue")
