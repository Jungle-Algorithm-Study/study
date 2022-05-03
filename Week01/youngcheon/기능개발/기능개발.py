from math import ceil
def solution(progresses, speeds):
    release = []
    # 배포되는 날짜 계산
    for p,s in zip(progresses, speeds):
        release.append(ceil((100-p)/s))
    # 첫 경우 제외하여 for문 시작
    count = 1
    k = release[0]
    result = []
    for i in release[1:]:
        # k값(첫값)보다 작으면 count + 1
        if k >= i:
            count += 1
        # 작으면 count를 result에 담고 k 값 갱신, count 초기화
        else:
            result.append(count)
            k = i
            count = 1
    result.append(count)
    return result