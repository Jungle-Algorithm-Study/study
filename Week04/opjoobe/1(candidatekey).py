# 후보키 # 5월20일 # sol 30min

# 두번째 풀이 (더 짧은 시간이 소요되는 개선된 풀이)
from itertools import combinations
'''
데이터베이스 용어 정리
row = tuple = student (여기선 student 로 사용)
column = attribute = field (여기선 attribute 로 사용)
'''
def solution2(relation):
    answer = 0
    attribute_n = len(relation[0])
    relation_n = len(relation)
    candidate_key_list = []

    # 최소성 검증 함수
    def is_minimal(key): 
        for candidate_key in candidate_key_list:
            if candidate_key.issubset(set(key)):
                return False
        return True

    # 유일성 검증 함수
    def is_unique(key):
        key_length = len(key)
        case_L = []
        for student in relation:
            case = ','.join([student[key[idx]] for idx in range(key_length)])
            if case in case_L:
                return False
            case_L.append(case)
        return True
    
    not_unique_attribute_list = list(range(attribute_n))
    
    '''하나의 컬럼만 가지는 싱글키(key)의 경우 최소성은 충족하니까, 유일성만 검증 후 충족하면 바로 추가'''
    for key in combinations(range(attribute_n),1):
        if is_unique(key):
            candidate_key_list.append(set(key)) 
            not_unique_attribute_list.remove(key[0]) # 홀로도 candidate_key가 된다면, 이후 combination에 포함될 필요 없도록.

    # print(not_unique_attribute_list) 
    '''두개 이상 컬럼 가지는 복합키(key)의 경우, 최소성 + 유일성 차례대로 모두 충족하면 후 추가'''
    for key_length in range(2, relation_n+1):
        for key in combinations(not_unique_attribute_list,key_length):
            if not is_minimal(key):
                continue
            if is_unique(key):
                candidate_key_list.append(set(key))

    answer = len(candidate_key_list) # 후보 키의 최대 개수
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution2(relation))

# 첫번째 풀이 (맨 처음 제출한 풀이)
from itertools import combinations
def solution(relation):
    answer = 0
    attribute_n = len(relation[0])
    relation_n = len(relation)
    candidate_key_list = []
    for i in range(1, relation_n+1):
        for key in combinations(range(attribute_n),i):
            print(key, type(key))
            flag = False
            for candidate_key in candidate_key_list:
                if candidate_key.issubset(set(key)):
                    flag = True
                    break
            if flag:
                continue
            case_D = dict()
            # print("case", key)
            for student in relation: # tuple 대신 student. (tuple은 지정어)
                L = list()
                for j in range(i):
                    attribute = key[j]
                    # print("a",attribute)
                    L.append(student[attribute])
                L = tuple(L)
                if L not in case_D.keys():
                    case_D[L] = 0
                case_D[L] += 1
            if not len([x for x in case_D.values() if x != 1]):
                candidate_key_list.append(set(key))
    answer = len(candidate_key_list)
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
