# 정답 코드
# DFS, 백트래킹 문제
# 풀이 영상: https://youtu.be/UTUShCoTPaM?si=GSx28d7HbmlmdEmG
def dfs(n, total):
    global answer

    # 가지치기
    if answer<=total:
        return
    
    # 종료조건
    if n==N:
        answer = min(answer, total)
        return

    for j in range(N):
        if visited[j]==0:
            visited[j]=1
            dfs(n+1, total+arr[n][j])
            visited[j]=0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 100
    visited = [0]*N
    dfs(0,0)

    print(f"#{test_case} {answer}")



