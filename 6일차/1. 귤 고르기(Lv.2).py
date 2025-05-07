# 1번째 코드: 시간 초과
def solution(k, tangerine):
    answer = 0
    tmp = 0
    t = list(set(tangerine))
    cnt = []
    
    for i in t:
        cnt.append(tangerine.count(i))

    cnt.sort(reverse=True)
    
    for i in cnt:
        if tmp >= k:
            break
        answer += 1
        tmp += i
    
    return answer

# 정답 코드: Dictionary 사용
# 출처: https://blog.naver.com/tmvmffpsej/223114403035
def solution(k, tangerine):
    answer = 0
    dic = {}
    r = 0
    
    # 딕셔너리에 key, value 형태로 값 넣음
    for i in tangerine:
        d = dic.get(i)
        if d == None:
            dic[i] = 1
        else:
            dic[i] += 1
    
    # value만 추출하여 내림차순으로 값 정렬
    dic = sorted(dic.values(), reverse=True)
    
    # k와 비교하며 count
    for i in dic:
        r += i
        answer += 1
        if k <= r: # k보다 같거나 크면 종료
            break
    return answer

# 더 효율적인 코드: Counter 사용
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
