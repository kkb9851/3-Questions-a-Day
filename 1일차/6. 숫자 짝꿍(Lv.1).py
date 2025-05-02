# 나의 풀이
# 시간 초과 코드
def solution(X, Y):
    ans = []
    max_ans = ""
    Y = list(Y)
    for c in X:
        if c in Y:
            ans.append(c)
            Y.remove(c)
            
    ans = list(map(int, ans))
    if not ans:
        return "-1"
    
    while ans:
        max_ans += str(max(ans))
        ans.remove(max(ans))
    
    if max_ans[0] == "0":
        max_ans = "0"
    
    return max_ans
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 정답 코드
# 1. 뭘 대상으로 반복문을 돌릴지... X? Y? no.. 0 ~ 9까지 10개만!
# 2. 정렬하지 않고도 자동으로 정렬이 되게 하는 법? (sort는 시간을 많이 잡아먹음..)
def solution(X, Y):
    answer = ''
    # ★ 포인트1. 반복되는 숫자를 저장하기 위한 dictionary (key: 0 ~ 9)
    numx = {str(n):0 for n in range(10)}
    numy = {str(n):0 for n in range(10)}
    
    # X 문자열 하나씩 돌면서 카운트
    for x in X:
        numx[x] += 1
    
    # Y 문자열 하나씩 돌면서 카운트
    for y in Y:
        numy[y] += 1
    
    # ★ 포인트2. 9부터 0까지 반복문 돌기. sort를 안 하기 위함.
    #           짝꿍을 큰 수부터 더해가면 자동으로 제일 큰 수가 됨.
    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(numx[k], numy[k])
        
        # ★ 포인트3. "000" -> "0"으로 만들어주기 위한 조건문
        if answer == '' and k == '0' and iternum != 0:
            return "0"
        
        # 실패 코드 #############################
        # for _ in range(iternum):             #
        #     answer = ''.join([answer, k])    #
        ########################################
        # 성공 코드 ★★★★★
        # '9'*3 = '999'가 되는 원리를 이용
        answer = ''.join([answer, k*iternum])  
        ########################################
    
    if answer == '':
        return "-1"
    else:
        return answer
출처: https://chan-lab.tistory.com/36 [은공지능 공작소:티스토리]

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 다른 풀이
def solution(X, Y):
    xList = list(X.count(str(x)) for x in range(10))
    yList = list(Y.count(str(y)) for y in range(10))
    answer = ""
    for i in range(9, -1, -1):
        answer += str(i) * min(xList[i], yList[i])

    if answer == "":
        return "-1"
    elif answer[0] == "0" and answer[len(answer) - 1] == "0":
        return "0"
    else:
        return answer
