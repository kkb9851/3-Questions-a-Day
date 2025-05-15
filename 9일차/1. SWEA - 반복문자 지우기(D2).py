# 나의 풀이
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()
    
    
    while True:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
                
        if ''.join(stack) == s:
            break
        else:
            s = ''.join(stack)
       
    print(f"#{test_case}", len(s))

# 다른 사람의 풀이
T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    s = 0
    while s < len(arr): # 이전 값과 비교하여 없애고 없애면 하나 전 인덱스로 이동해 다시 확인
        if s and arr[s] == arr[s-1]:    # s가 0이 아닐 때 이전 값과 비교
            del arr[s], arr[s-1]    # 같을 땐 값을 지우고 이전 인덱스로 이동해 비교한다.
            s -= 1
        else:   # 다를 땐 다음 인덱스로 이동한다.
            s += 1
    print(f'#{tc} {len(arr)}')
