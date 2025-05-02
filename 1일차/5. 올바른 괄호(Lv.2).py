# 나의 풀이
def solution(s):
    cnt = 0
    for c in  s:
        if c == ')':
            if cnt == 0:
                return False
            else:
                cnt -= 1
        else:
            cnt += 1
            
    if cnt == 0:
        return True
    else:
        return False

# 베스트 풀이
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair("()()()"))
