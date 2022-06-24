# 프로그래머스 #비밀지도

# 두번째 풀이 # 개선
def solution(n, arr1, arr2):
    def encode_num(target):
        return bin(target)[2:].zfill(n).replace('0',' ').replace('1','#')
    def full_map(n1,n2):
        return ''.join(['#' if s1 =='#' or s2 =='#' else ' ' for s1,s2 in zip(n1,n2)])
    return [full_map(encode_num(n1), encode_num(n2)) for n1,n2 in zip(arr1,arr2)]
    

# 첫번째 풀이 # 20min sol
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        n1, n2 = arr1[i], arr2[i]
        new_n1, new_n2 = bin(n1)[2:], bin(n2)[2:]
        len1 = len(new_n1)
        len2 = len(new_n2)
        if len1 < n:
            new_n1 = '0'*(n-len1) + new_n1
        if len2 < n:
            new_n2 = '0'*(n-len2) + new_n2
        
        now_line = ''
        for j in range(n):
            if new_n1[j] =='0' and new_n2[j] == '0':
                now_line += ' '
            else:
                now_line += '#'
        answer.append(now_line)
            
    return answer