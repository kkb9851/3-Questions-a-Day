# 나의 풀이
# format 대신 bin함수를 이용하는 방식도 존재
def solution(n):
    ans = n+1
    n_two = format(n, 'b')
    
    while True:
        ans_two = format(ans, 'b')
        if str(n_two).count('1') == str(ans_two).count('1'):
            return ans
        ans += 1

# 다른 사람의 풀이 (비트 연산자)
def solution(n):
    pivot = n & -n;
    before = ((n ^ (n + pivot)) // pivot) >> 2;
    return (n + pivot) | before;  
