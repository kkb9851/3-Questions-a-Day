# 트리(Tree): 대표적인 비선형 자료구조, 그래프(Graph)의 특수한 형태
# 방향성과 계층성, 단일 경로, 사이클 없음


# 클래스 기반의 트리 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 트리 순회의 방식 
# 1. 깊이 우선 탐색(DFS)
def preorder(node):
    # 전위 순회 (Pre-order)
    # 루트 → 왼쪽 → 오른쪽
    if node:
        visit(node)  # 방문 처리
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    # 중위 순회 (In-order)
    # 왼쪽 → 루트 → 오른쪽
    if node:
        inorder(node.left)
        visit(node)  # 방문 처리
        inorder(node.right)

def postorder(node):
    # 후위 순회 (Post-order)
    # 왼쪽 → 오른쪽 → 루트
    if node:
        postorder(node.left)
        postorder(node.right)
        visit(node)  # 방문 처리


# 2. 너비 우선 탐색 (BFS): 큐(Queue)를 활용하여 레벨 단위로 순회
from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        visit(node)  # 방문 처리
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
