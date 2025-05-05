# 1번째 풀이: 시간 초과
import string

def solution(s):
    lower = [i for i in string.ascii_lowercase]
    
    while s:
        cnt = 0
        for c in lower:
            if c*2 in s:
                s = s.replace(c*2, '')
                cnt += 1
                
        if cnt == 0:
            break
                
    if not s:
        return 1
    else:
        return 0

# 2번째 풀이: Stack 사용 (올바른 괄호 문제와 동일!!)
def solution(s):
    s1 = []

    for c in s:
        if s1 and s1[-1] == c:
            s1.pop()
        else:
            s1.append(c)
    
    if s1:
        return 0
    else:
        return 1

# 다른 사람의 풀이
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0
