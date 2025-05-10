# 스택(Stack):  한쪽 끝에서만 자료의 삽입과 삭제가 가능한 선형 자료구조
# 삽입: push, 삭제: pop
# 스택 예제: 괄호 구조 판단, 괄호 계산 순서 결정, 스택으로 수열 만들기 등

# 스택 기본 연산
stack.append(data)  # push
stack.pop()         # pop

# 클래스 기반의 스택 구현
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("empty stack")

    def size(self):
        return len(self.items)
      
