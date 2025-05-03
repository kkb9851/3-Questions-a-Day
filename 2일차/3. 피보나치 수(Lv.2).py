# 나의 풀이
def solution(n):
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    
    return fibo[-1] % 1234567


# 다른 사람의 풀이
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
