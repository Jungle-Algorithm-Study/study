# 순위 검색 
# 풀이날짜 5월 3일 # 정확성 sol 20min # 효율성 fail 60min # 해당코드: solution2
# 풀이날짜 5월 4일 # sol 50min # 카카오에서 제시한 해설 참고 후 재도전 # 해당코드: solution1

'''
카카오에서는 대략 아래와 같이 해설을 제시하였습니다.

1. info에 대해 '-'를 추가한 모든 경우의 수를 만들어 해쉬테이블에 넣는다.
2. query를 불러와 데이터를 파싱한 후 해쉬테이블에 key로써 접근하여 score데이터를 가져온다.
3. score데이터를 이진탐색을 사용하여 기준이상의 데이터의 개수를 센다.(lower bound 사용)
4. 순서대로 값을 반환한다.
'''

info = ["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150","cpp backend senior pizza 260",
"java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]


'''풀이 1 (5월 3일)'''
# 효율성 잡지 못한, 기존 코드 -> solution1 # 실패
# * [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
# '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.

def solution1(info, query):
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
print("solution1",solution1(info,query))

'''풀이 2 (5월 4일)'''
# 카카오에서 제시한 해설에 기반해 짜본 새로운 코드 -> solution2 # 통과

def solution2(info, query):
    answer = []

    languages = ['cpp', 'java', 'python', '-']
    jobs = ['backend', 'frontend', '-']
    careers = ['junior', 'senior', '-']
    soulfoods = ['chicken', 'pizza', '-']
    # make hash table by combination
    # make DB for SQL queries

    DB = dict()

    for language in languages:
        for job in jobs:
            for career in careers:
                for soulfood in soulfoods:
                    DB[language+' '+job+' '+career+' '+soulfood] = list()

    info_length = len(info)

    for i in range(info_length):
        now_info = info[i].split(' ')    
        now_language = now_info[0]
        now_job = now_info[1]
        now_career = now_info[2]
        now_soulfood = now_info[3]
        now_score = now_info[4]
        joker = '-'
        # 16 combinations from 1 now_info -> each 16 queries get now_score in its own list()
        for language in (now_language, joker):
            for job in (now_job, joker):
                for career in (now_career,joker):
                    for soulfood in (now_soulfood, joker):
                        DB[language+' '+job+' '+career+' '+soulfood].append(int(now_score))
    
    # sort each list, which has scores w/ given condition
    for key in DB.keys():
        DB[key].sort()

    query_length = len(query)

    for i in range(query_length):
        # print(f"{i}번째 query: {query[i]}")
        now_query = query[i].rsplit(' ',1)
        # print(f"now_query = {now_query}")
        now_condition, now_cutline_score = now_query[0].replace(' and ', ' '), int(now_query[1])
        # print(f"now_condition = {now_condition}, now_cutline_score = {now_cutline_score}")
        now_score_list = DB[now_condition]
        # print(f"now_score_list = {now_score_list}")
        now_score_list_length = len(now_score_list)
        left = 0
        right = now_score_list_length-1
        while left <= right:
            mid = (left+right)//2
            if now_score_list[mid] >= now_cutline_score:
                right = mid-1
            else:
                left = mid+1
        # right => biggest idx possible, when now_score_list[idx] < now_cutline_score 
        now_query_satisfying_applicant_cnts =now_score_list_length-1-right # len(DB[right+1:]) len(now_score_list)-1 - right
        answer.append(now_query_satisfying_applicant_cnts)

    return answer

print("solution2",solution2(info,query))


'''풀이 3 (공부용) '''
# library를 활용한 짧은 코드 -> solution3 (https://programmers.co.kr/questions/27124)

import bisect, itertools, collections

def solution3(info, query):
    infomap = collections.defaultdict(list) # solution2의 DB생성을 위한 4중포문을 대체함 # 사전을 미리 만들지않고, defaultdict로 선언만 해둠
    binarys = list(itertools.product((True, False), repeat=4)) # solution2 의 for i in range(info_length)를 대체하기 위함
    for inf in info:
        inf = inf.split()
        for binary in binarys: # solution2 의 for i in range(info_length)를 대체
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4])) # 해당 키가 있을때마다 defaultdict를 활용해 키 생성 & score 추가를 병행

    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split() # and 를 underscore으로 무시해주고 필요한 것만 취함
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point)) # left,right,mid 를 활용한 binary_search를 정확히 같은 기능을 제공하는 bisect_left로 대체함
        # solution2의 right+1 = bisect_left(infomap[key],int(point)) = i
        answers.append(len(infomap[key]) - i) # len(infomap[key])-1 -(i-1) = len(infomap[key])-i
    return answers

print("solution3",solution3(info,query))

