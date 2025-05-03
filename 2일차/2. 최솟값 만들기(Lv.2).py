# 나의 풀이
def solution(A,B):
    ans = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        ans += A[i] * B[i]
    return ans

# 정답 코드(한줄 코드)
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
