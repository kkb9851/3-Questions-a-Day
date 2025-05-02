#나의 풀이
def solution(a, b):
    sum = 0
    if a > b:
        for i in range(b, a+1):
            sum += i
    else:
        for i in range(a, b+1):
            sum += i
    return sum

#베스트 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    #sum() 함수 활용
    return sum(range(a, b + 1))

#아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
