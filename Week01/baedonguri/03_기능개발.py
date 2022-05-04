from math import ceil

def solution(progresses, speeds):
    arr = []
    answer = []
    idx = 0
    
    # 기능 개발에 걸리는 각 일자를 계산
    for p, s in zip(progresses, speeds):
        arr.append(ceil((100-p)//s))
    
    for i in range(len(arr)):
        if arr[idx] < arr[i]: #시작 기준으로 뒤에 큰 날짜가 있기 전까지 
            answer.append(i-idx) # 몇개가 있는지 계산
            idx = i #해당 index부터 시작하기 위해 idx변수를 갱신
    answer.append(len(arr)-idx) #마지막 요소까지 계산

    return answer

# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(solution([96,94],[3,3]))