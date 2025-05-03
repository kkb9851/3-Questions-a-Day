# 효율성 테스트 fail -> del을 이용해 리스트 원소를 제거하는 작업은 O(N)의 시간복잡도를 가집니다.
# 결과: 타임 아웃
def solution(people, limit):
    tmp = 0
    cnt = 0
    people.sort(reverse=True)
    
    while people:
        tmp += people[0]
        del people[0]
        for i in range(len(people)):
            if tmp + people[i] <= limit:
                cnt += 1
                tmp = 0
                del people[i]
                break
        if tmp != 0:
            cnt += 1
            tmp = 0
        
    return cnt

# 정답 코드
# 출처: https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-Python
from collections import deque # deque 사용

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer

