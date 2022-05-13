from itertools import combinations
from collections import defaultdict
import bisect
def solution(infos, query):
    # 들어온 데이터 전처리
    query = [i.replace('and','').split() for i in query]
    infos = [i.split() for i in infos]

    info_dict = defaultdict(list)

    # 가능한 모든 경우의 수를 계산하여 조건에 따라 점수를 딕셔너리 형태로 저장
    # 즉 : pythonjuniorchicken = [150,50,300]
    for info in infos:
        for i in range(5):
            for j in combinations(info[:-1],i):
                info_dict[''.join(j)].append(int(info[-1])) 

    for i in info_dict:
        # 점수 정렬
        info_dict[i].sort()

    answer = []

    # 이진탐색
    for i in query:
        # 1) 점수
        score = int(i[-1])
        # 쿼리의 '-'를 ''으로 치환하여 하나의 문장으로 만듬
        # 예를 들어 pythonjuniorchicken
        result = ''.join(i[:-1]).replace('-','')
        # 일치하는 쿼리의 인원을 ans에 저장
        ans = info_dict[result]
        # 1)점수 이상의 인원을 찾아야하기 때문에 전체 인원 - 점수 이하의 인덱스를 수행
        answer.append(len(ans)-bisect.bisect_left(ans,score))

    return answer


## 검색해서 풀었습니다.