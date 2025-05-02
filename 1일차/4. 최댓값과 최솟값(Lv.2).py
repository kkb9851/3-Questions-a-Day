# 나의 풀이
def solution(s):
    # list의 문자열을 int 형태로 변형
    num = list(map(int, s.split(" ")))
    ans = str(min(num)) + ' ' + str(max(num))
    return ans

# 베스트 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
