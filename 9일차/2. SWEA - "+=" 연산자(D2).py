# 나의 풀이
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, n = map(int, input().split())
    cnt = 0
        
    while a <= n:
        if a > b:
        	a, b = b, a
        a += b
        cnt += 1
        
    print(cnt)

# 다른 사람의 풀이
test_case = int(input())
for _ in range(test_case):
    a, b, n = map(int, input().split())
    cnt = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        cnt += 1
    print(cnt)
