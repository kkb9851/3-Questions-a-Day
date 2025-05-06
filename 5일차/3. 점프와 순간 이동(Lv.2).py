# 나의 풀이
def solution(n):
    ans = 0
    
    while n > 0:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ans += 1

    return ans

# 다른 사람의 풀이 1
def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer

# 다른 사람의 풀이 2
def solution(n):
    return bin(n).count('1')
