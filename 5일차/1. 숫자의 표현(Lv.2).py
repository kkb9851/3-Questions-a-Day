# 시간 초과
def solution(n):
    answer = 1
    tmp = [i for i in range(1, n+1)]   
    
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if sum(tmp[i:j]) == n:
                answer += 1
    
    return answer

# 정답 코드
# 출처: https://1ets-just-do-it.tistory.com/109
def solution(n):
    answer = 1

    # 1부터 n의 절반까지 순회
    # 연속된 자연수들의 합이 n을 초과하는 경우는 고려하지 않기 때문
    for i in range(1, n // 2 + 1):
        total = 0
        
        while total < n:
            total += i
            
            if total == n:
                answer += 1
                break
                
            i += 1     
    
    return answer

