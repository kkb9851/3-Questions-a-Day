# 나의 풀이
T = int(input())
cnt = 1

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
   	
    for _ in range(M):
        tmp = a.pop(0)
        a.append(tmp)
    
    print(f"#{cnt}", a[0])
    cnt += 1

# 다른 사람의 풀이: deque 활용법
from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    i = 0
    while i < M:
        back = arr.popleft()
        arr.append(back)
        i += 1

    print('#{} {}'.format(tc, arr[0]))
