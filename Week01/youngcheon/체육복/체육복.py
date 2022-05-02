def solution(n, lost, reserve):
    # 중복 제거
    lo = set(lost)-set(reserve)
    res = set(reserve) - set(lost)
    
    case1 = lo-set(map(lambda x: x+1, res))
    case2 = lo-set(map(lambda x: x-1, res))
    temp = []
    for i in lo:
        if list(res).count(i-1):
            res.remove(i-1)
            temp.append(i)
    for i in lo:
        if list(res).count(i+1):
            res.remove(i+1)
            temp.append(i)
    case3 = lo-set(temp)
    answer = min(len(case3),len(case1),len(case2))
    return n - answer

# 케이스1 = 왼쪽사람에게 빌려주기
# 케이스2 = 오른쪽사람에게 빌려주기
# 케이스3 = 잃어버린사람중에 빌려줄 사람 찾은 사람 뺀거
# 뭔가 더 깔끔하게 짤 수 있을거같은데 반례를 하나하나 적용하다보니
# 하나라도 빼면 틀려버림... 나중에 다시 짜봐야겠다