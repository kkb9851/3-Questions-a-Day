# 1번째 코드(오답)
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
    s = s.split(' ')
    ans = []
    
    for i in s:
        ans.append(i.capitalize())
        
    return ' '.join(ans)
