# 틀린 풀이
def solution(n, words):
    answer = [0, 0]
    
    for i in range(1, len(words)):
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
            answer[0] = (i + 1) % n
            answer[1] = len(words) // n
            return answer
    return answer

# 정답 풀이
# 출처: https://siloam72761.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%98%81%EC%96%B4-%EB%81%9D%EB%A7%90%EC%9E%87%EA%B8%B0
def solution(n, words):
    
    checked = [words[0]]
    
    for i in range(1,len(words)):
        #i번째 단어와 첫 글자와 i-1번째 단어의 마지막 글자랑 비교 
        if words[i][0] == words[i-1][-1] and words[i] not in checked:
            checked.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]

    return [0,0]

# 다른 풀이
def solution(n, words):
    
    for i in range(1, len(words)):
        #글자가 맞지 않을 때
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    
    return [0,0]
