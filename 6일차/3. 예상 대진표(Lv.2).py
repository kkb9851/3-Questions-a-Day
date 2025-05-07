# 나의 풀이
def solution(n,a,b):
    answer = 0
    
    while True:
        answer +=1
        
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
            
        if a // 2 == b // 2:
            break
            
        a /= 2
        b /= 2

    return answer

# 다른 사람의 풀이
def solution(n,a,b):
    answer = 0
    while a != b:
        # 매번 홀수번째와 짝수번째가 붙는데 이때 홀수가 더 작은 쪽
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
