# 정답 코드
# https://ror-coding.tistory.com/84
import math
def solution(arr):
    
    while len(arr) >= 2:
        a, b = arr[0], arr[1]
        # 유클리드 호제법
        arr.append((a*b) // math.gcd(a,b))
        arr = arr[2:]
        
    return arr[0]
