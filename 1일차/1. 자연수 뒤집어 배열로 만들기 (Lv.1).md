#나의 풀이
def solution(n):
    answer = []
    s = str(n)
    for i in s:
        answer.append(int(i))
    answer.reverse()
    return answer

#베스트 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
