# 프로그래머스 # 영어 끝말잇기 # 20min sol 생각보다 오래걸림

# 첫번째 풀이 개선의 개선
def solution(n, words):
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0] or words[idx] in words[:idx]:
            return list(map(lambda x:x+1,divmod(idx,n)))[::-1]
    return [0,0]
    
# 첫번째 풀이 개선
def solution(n, words):
    last_char = words[0][0]
    for now_idx in range(len(words)):
        now_word = words[now_idx]
        if last_char != now_word[0] or now_word in words[:now_idx]:
            return list(map(lambda x:x+1,divmod(now_idx,n)))[::-1]
        else:
            last_char = now_word[-1]
    return [0,0]

# 첫번째 풀이
def solution(n, words):
    answer = []
    before_word = words[0][0]
    words_length = len(words)
    for now_idx in range(words_length):
        if now_idx >= len(words):
            break
        # now_person = now_idx % n
        now_word = words[now_idx]
        # print(now_word, before_word)
        if before_word[-1] != now_word[0] or now_word in words[:now_idx]:
            # print(before_word[-1])
            # print(now_word[0])
            cnt, now_person = divmod(now_idx,n)
            # print(now_idx)
            answer = [now_person+1, cnt+1]
            break
        else:
            before_word = now_word[-1]

    if not answer:
        answer = [0,0]

    return answer
