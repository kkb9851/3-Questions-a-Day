# 나의 풀이
def solution(brown, yellow):
    carpet = brown + yellow
    
    for h in range(3, carpet + 1):
        if carpet % h == 0:
            w = carpet // h
            if (w-2) * (h-2) == yellow:
                return [w, h]

    return -1


# 다른 사람의 풀이
# 출처: https://school.programmers.co.kr/questions/52491
# x * y = brown + yellow
# x + y = (brown + 4)//2

# x + y 에서 x, y를 정한다. 이때 x와 y의 차가 작을 수록 그 곱은 더 커진다.
# 이를 이용해서 이분 탐색으로 그 차의 크기를 조절해서 답을 구한다.

# x <= y 라고 하면, x는 1 ~ (x+y)//2 의 값을 가진다.
def solution(brown, yellow):
    m = brown + yellow
    s = (brown + 4) // 2

    # x가 가질 수 있는 최대값
    diff = (s // 2)

    # x가 가질 수 있는 최대값의 절반
    x = diff // 2
    y = s - x
    diff //= 2

    while x * y != m:
        if diff != 1:
            diff //= 2

        if x * y > m:
            x -= diff
            y += diff

        else:
            x += diff
            y -= diff

    return [y, x]
