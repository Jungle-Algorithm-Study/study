# 순위 검색 # 풀이날짜 5월 3일 # 정확성 sol 20min # 효율성 fail 60min # 5월 5일 재도전예정

# * [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
# '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.

def solution(info, query):
    answer = []
    info = [x.strip().split() for x in info]
    info.sort(key=lambda x: int(x[-1]))
    info_Length = len(info)

    for case in query:
        case = case.strip().rsplit(' ',1)
        testScore = case[1]
        case = case[0].split(' and ')

        check = []
        for i in range(4):
            if case[i] != '-':
                check.append(i)

        left = 0
        right = info_Length-1
        while left <= right:
            mid = (left+right)//2
            if int(info[mid][-1]) < int(testScore):
                left = mid+1
            else:
                right = mid-1
        cnt = 0
        for appliant in info[right+1:]:
            for idx in check:
                if case[idx] != appliant[idx]:
                    break
            else:
                    cnt += 1
        answer.append(cnt)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))



# print(query[3])

# info = [x.strip().split() for x in info]
# print(info[0])
# info.sort(key=lambda x: int(x[-1]))
# left = 0
# right = len(info)
# key = 1
# while left<right:
#     mid = (left+right)//2
#     if info[mid] <= key:
#         left = mid+1
#     else:
#         right = mid-1