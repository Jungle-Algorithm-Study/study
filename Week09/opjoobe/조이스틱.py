#프로그래머스 #조이스틱 # 110min sol

# 완성해야 하는 이름 길이만큼 'A'로 채워진 것이 주어짐
# Up : 다음
# Down : 이전 (A의 Down은 Z)
# Left : 커서 왼쪽으로 이동 (첫번째 문자에서 이동하면 마지막으로)
# Right: 커서 오른쪽으로 이동 (마지막 문자에서 이동하면 첫번째로)

# 커서 이동을 최소화 (Left로 가는게 빠른지, Right으로 가는게 빠른지)
# 알파벳 만들때도 최소화 (Up으로 가는게 빠른지, Down으로 가는게 빠른지)

def solution(name):
    answer = 0 # 총 조작횟수
    Alpha_D = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
    def change_alpha(start):
        start = Alpha_D[start]
        # end = 0 # Alpha_D['A']
        n1, n2 = start, 26 - start
        return n1 if n1 < n2 else n2
    def change_cursor(L, n):
        all_right = L[-1]
        all_left = n - L[0]
        if len(L) == 1:
            return min([all_right, all_left])
        mix1 = n
        mix2 = n
        max_A = 0
        max_idx = []
        before = 0
        for now in L:
            if max_A < now - before:
                max_idx = [before, now]
                max_A = now - before
            before = now
        ''' 조건문 확인 없이 mix1과 mix2를 다 구해야한다. why..? '''
        # if L[-1] - max_idx[0] >= (n - max_idx[1]) * 2:
        mix1 = (n - max_idx[1]) * 2 + max_idx[0]
        mix2 = max_idx[0] * 2 + (n - max_idx[1])
        M = [all_right, all_left, mix1, mix2]
        return min(M)
            
    ''' 전체가 다 A로 구성된 경우'''
    N = len(name)
    if name.count('A') == N:
        return 0
    
    not_A = []
    for i in range(N):
        if name[i] == 'A': continue
        not_A.append(i)

    # 알파벳 조작하는 횟수 더해주기
    for i in not_A:
        target = name[i]
        answer += change_alpha(target)
    # 커서 좌우로 옮기는 횟수 더해주기 -_- 더러워
    if 0 in not_A:
        not_A.remove(0)
    if not not_A:
        return answer
    answer += change_cursor(not_A, N)
        
    return answer