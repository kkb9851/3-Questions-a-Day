# 나의 풀이
def solution(arr):
    answer = []
    for i in arr:
        # answer가 비어 있는 경우를 먼저 체크
        if not answer or i != answer[-1]:
            answer.append(i)
    return answer

# 다른 사람의 풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
