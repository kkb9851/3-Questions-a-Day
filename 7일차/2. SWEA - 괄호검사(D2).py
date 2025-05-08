# 1번째 풀이: 오답 (Runtime error)
T = int(input())

for test_case in range(1, T + 1):
    str = input()
    stack = []
    
    for c in str:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                break
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                break
                
    if not stack:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")


# 2번째 풀이: 오답 (break의 발생 여부 체크 안함)
T = int(input())

for test_case in range(1, T + 1):
    str = input()
    stack = []
    
    for c in str:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')':
            if not stack:
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                break
        elif c == '}':
            if not stack:
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                break
                
    if not stack:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")


# 3번째 풀이: 정답
T = int(input())

for test_case in range(1, T + 1):
    str = input()
    stack = []
    check = 0 # Break 발생 여부 체크
    
    for c in str:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')':
            if not stack:
                check += 1
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                break
        elif c == '}':
            if not stack:
                check += 1
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                break
                
    if not check and not stack:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")


# 다른 사람의 풀이
# 출처: https://totoma3.tistory.com/128
Test_case=int(input())

for t in range(1, Test_case+1):
    stack=[]                   
    ans=1
    string=str(input()) #문자열 입력
    arr=list(string)    #리스트 사용
    for i in range(0, len(arr)):   
        if arr[i]=='(' or arr[i]=='{':  #만약 arr에 (나 {가 나오면
            stack.append(arr[i])        #만들어두었던 stack에 추가
        elif arr[i]==')' or arr[i]=='}': #아니면 arr가 )나 }가 나왔을때
            if not stack:                #stack이 비어있는데
                ans=0                    #ans=0과 동시에
                break                   #멈춤

            P=stack.pop()                #stack에서 pop하는 것을 P로 지정
            if arr[i] == ')' and P!='(': #만약 arr가 )이거나 pop한게 (가 아니면 즉 ()가 성립 안하게 되는 경우
                ans=0                    #ans=0이 나오도록
            elif arr[i]=='}' and P!='{':  #만약 arr가 }이거나 pop한게 {가 아니면 즉 {}가 성립 안하게 되는 경우
                ans=0                     #ans=0
    if stack:                             #만약 stack이면
        ans=0                             #ans=0
    print("#{} {}".format(t,ans))  
