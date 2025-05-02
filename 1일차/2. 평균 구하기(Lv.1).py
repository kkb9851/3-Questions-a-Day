#나의 풀이
def solution(arr):
    return sum(arr)/len(arr)

#베스트 풀이
def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    return sum(list) / len(list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
