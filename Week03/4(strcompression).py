# 프로그래머스 # 문자열 압축 # 25min sol
# 첫 풀이에서 변수명만 좀 바꾸고, 주석 추가했어유
def solution(s):
    s_length = len(s)
    answer = s_length
    # 자르는 단위는 1 ~ 문자열 s의 절반 길이 까지 (절반길이보다 크게는 자르는 의미가 없음)
    for i in range(1,s_length//2+1):
        cut = i # cut은 자르는 단위
        cut_i_compressed_str = '' # i개 단위로 잘랐을 때의 압축문자열
        target = s[:cut] # 압축 타겟을 첫번째 단위문자열로 지정
        cnt = 1 # 반복횟수
        for j in range(cut, s_length, cut): # s[:cut]은 초기화하며 이미 처리했으니, 그 이후부터 잘라가며 확인
            start, end = j, j+cut 
            if end > s_length:
                end = s_length
            now = s[start:end] # i 길이로 잘라준 현재의 단위문자열
            # print(now)
            if target == now: # 직전과 똑같은 단위문자열이 연속되고 있다면 반복횟수 1 증가
                cnt += 1
            else: # 연속이 종료되었다면, 그동안의 쌓인걸 압축처리해주고 초기화
                if cnt > 1:
                    cut_i_compressed_str += str(cnt)
                cut_i_compressed_str += target
                # 압축 타겟 및 반복횟수 초기화
                target = now
                cnt = 1
        # 마지막으로 남은 압축 타겟 및 반복횟수 반영
        if cnt > 1:
            cut_i_compressed_str += str(cnt)
        cut_i_compressed_str += target
        # print(f"cut = {cut}일때, 압축문자열: {cut_i_compressed_str}")
        cut_i_compressed_length = len(cut_i_compressed_str)
        # 압축문자열 최소길이 업데이트
        if answer > cut_i_compressed_length:
            answer = cut_i_compressed_length
    return answer

s = 'abcabcabcabcdededededede'
print(solution(s))
# for i in range(0, 19, 3):
#     print(i)
