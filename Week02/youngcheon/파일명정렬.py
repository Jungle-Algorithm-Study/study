import re
def solution(files):
    result = []
    for file in files:
        number = re.findall('\d+',file)[0]
        head = file.split(number)[0]
        result.append([file,head,number])
    result.sort(key= lambda x: (x[1].lower(), int(x[2])))
    return list(map(lambda x: x[0], result))

'''
처음에 TAIL도 정렬해야 하는 줄 알고 스트레스 받았는데
알고보니 HEAD, NUMBER만 정렬해주면 된다.

따라서 NUMBER는 정규식을 이용해서 떼어주고,
HEAD는 NUMBER로 split한 결과물에 0번째이므로,
원본 파일명과 HEAD, NUMBER 을 리스트에 넣어준뒤
lower된 HEAD,(대소문자를 구분하지 않기때문에)
int형 변환된 NUMBER (앞에 0을 떼어줘야 하기 때문에)
을 기준으로 sort한뒤 (파이썬은 기본적으로 파일명이 똑같으면 인덱스 순으로 정렬한다)
원본 파일명만 출력하면 된다.
'''