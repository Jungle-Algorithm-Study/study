# 수식 최대화 # 시작 2시 6분 # 끝 3시 34분 # sol 86min
import itertools

# 성공한 풀이 # 3시 10분 시작 # 3시 34분 끝 #..........
'''
expression = 50*6-3*2
우선순위가 * > - 인 경우

['50',*,'6',-,'3',*,'2']
['300',-,'3',*,'2']
['300',-,'6']
['294'] 

이 되도록 코드를 구성해보자
'''
def solution(expression): 
    exp_length = len(expression)
    expression_list = []
    answer = 0
    num_idx = 0
    for exp_idx in range(exp_length):
        case = expression[exp_idx]
        if not case.isdigit():
            # 연산자
            expression_list.append(expression[num_idx:exp_idx]) # 번호뽑기
            expression_list.append(case) # 연산자뽑기
            num_idx = exp_idx+1
    expression_list.append(expression[num_idx:]) # 마지막 한 숫자 처리
    unique_op = set(x for x in expression_list if not x.isdigit())

    for c in itertools.permutations(unique_op,len(unique_op)):
        now_list = expression_list.copy()
        for operator in c:
            idx = 1
            while idx < len(now_list):
                if now_list[idx] == operator:
                    n1 = int(now_list[idx-1])
                    n2 = int(now_list[idx+1])
                    if operator == '+':
                        new = [str(n1+n2)]
                    elif operator == '-':
                        new = [str(n1-n2)]
                    else:
                        new = [str(n1*n2)]
                    now_list = now_list[:idx-1] + new +now_list[idx+2:]
                    idx = 1 # 해당 연산자가 있으면, 처리해주고 다시 while문 돌리기 위해 idx 변수 초기화
                else:
                    idx += 2 # 해당 연산자가 없으면 이 +2를 타고 넘어가다가 결국 while문이 종료되고, 다음 연산자를 for문으로 돌림
        now_ans = abs(int(now_list[0])) # 예시에서 ['294']가 남았으면 그걸 뽑아오는 과정
        answer = max(answer, now_ans) # 더 큰 결과가 있으면 업데이트
    return answer

expression = "100-200*300-500+20" #60420
expression2 = "50*6-3*2" # 300
expression3 = "50+1-4" # 47

print(solution(expression))


###################
# 실패한 풀이 # 시작 2시 6분 # 포기 3시 10분
import itertools
    
def solution(expression): 
    exp_length = len(expression)
    operators = [] # idx, type
    numbers = []
    answer = 0
    op_idx = 0
    num_idx = 0
    for exp_idx in range(exp_length):
        case = expression[exp_idx]
        if not case.isdigit():
            # 연산자
            numbers.append(int(expression[num_idx:exp_idx])) # 번호뽑기
            operators.append([exp_idx, case, op_idx]) # 연산자뽑기
            op_idx += 1
            num_idx = exp_idx+1
    numbers.append(int(expression[num_idx:])) # 마지막 한 숫자 처리
    N = op_idx   
    unique_op = set(x[1] for x in operators)
    print(unique_op)

    for c in itertools.permutations(unique_op,len(unique_op)):
        numbers_copy = numbers.copy()
        # c = ('*','+','-')
        priority_D = {k:v for k,v in zip(c,list(range(3)))}
        operators.sort(key=lambda x: (priority_D[x[1]],x[0]))
        # print(operators)
        # print(c)
        visited = [0]*(op_idx+1)
        for now in operators:
            
            # print(now)
            operator = now[1]
            number_guide = now[2]
            left = number_guide
            while visited[left] and left > 0:
                left -= 1
            n1 = numbers_copy[left]
            n2 = numbers_copy[number_guide+1]
            # print(n1, operator, n2)
            if operator == '+':
                new_number = n1+n2
            elif operator == '-':
                new_number = n1-n2
            else: # *
                new_number = n1*n2
            numbers_copy[left] = new_number
            numbers_copy[number_guide+1] = new_number
            visited[left] = 1
            visited[number_guide+1] = 1
            # print(visited)
            # print(numbers_copy)
        now_ans = abs(new_number)
        answer = max(answer, now_ans)
    return answer
