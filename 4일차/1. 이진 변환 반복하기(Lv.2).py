# 나의 풀이
# s.pop('0')을 쓸 경우 TypeError: 'str' object cannot be interpreted as an integer 발생
# 원인: pop()함수는 정수형 인덱스를 인자로 받아야 하기 때문
def solution(s):
    ans = [0, 0]
    
    while s != '1':
        cnt = 0
        len_s = 0
        
        cnt = s.count('0')
        s = s.replace('0', '')
        
        len_s = format(len(s), 'b')
        s = str(len_s)
        ans[0] += 1
        ans[1] += cnt
        
    return ans

# 다른 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
