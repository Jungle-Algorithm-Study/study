from math import ceil
def solution(n, words):
    last = words[0][-1] # 첫번재 단어 끝글자
    mafia, order = 0,0 # 범인, 순서
    for e, word in enumerate(words[1:],2):
        # 끝말잇기가 되지 않거나 말했던 단어라면
        if word[0] != last or word in words[:e-2]:
            mafia = n if e%n == 0 else e%n # 나머지가 0이면 n이 범인임
            order = ceil(e/n)
            break
        last = word[-1] # 끝단어 갱신
    return [mafia, order]