# 1번째 코드(오답)
# split()에서 인자를 주지 않을 경우: 연속된 공백을 하나로 처리
def solution(s):
    words = []
    ans = []
    
    s = s.lower()
    words = s.split()
    
    for c in words:
        ans.append(c.capitalize())
    
    return ' '.join(ans)

# 2번째 풀이 코드
def solution(s):
    s = s.lower()
    # split(' '): 정확히 스페이스 한 칸만 구분자로 사용 
    s = s.split(' ')
    ans = []
    
    for i in s:
        ans.append(i.capitalize())
        
    return ' '.join(ans)
