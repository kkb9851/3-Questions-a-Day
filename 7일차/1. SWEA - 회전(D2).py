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

# 다른 사람의 풀이
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    
    for i in range(m):
        queue.append(queue.pop(0))
    
    print('#{} {}'.format(test_case, queue[0]))
