import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
# re.compile("정규표현식") 형태로 사용한다.
# pat은 패턴 객체. p로도 많이 사용함
print(pat.sub("\g<1>-*******", data))


##### match

p = re.compile('[a-z]+') # a~z 중 무언가가 1번이상 반복되는 경우
l = p.match('python')
m = p.match('python3')
n = p.match('3python') # match 객체가 안나옴
print(l, m, n, sep='\n')

##### search : 꼭 첫번째부터 일치하지 않아도, 그 결과를 돌려줌,

a = p.search('3python')
print(a)

##### findall

p = re.compile('[a-z]+')
m = p.findall('life is too short')




"""
문자 클래스
- [] 사이의 문자들과 매치가 된다.
- 하이픈을 사용하여 From-To로 표현이 가능하다.
[a-c] = [abc] / [0-5] = [012345]
"""

"""
Dot(.)
- 줄바꿈(\n)을 제외한 모든 문자와 매치가 가능하다.
- a.b 
- aab, a0b 등 a와 b 사이에 무엇이 들어오든 다 매치가 가능하다
- abc, abd 등 a와 b 사이에 단 한 문자도 없다면 매치되지 않는다
"""

"""
반복(*)
- 0번 반복되어도 매치된다는게 특징이다.
- ca*t
- ct (0번반복), cat (1번반복), caaat (3번반복) 모두 매치가 된다
"""

"""
반복(+)
- 0번 반복되는경우 매치되지 않는다.
- ca+t
- ct (0번반복)는 매치되지 않음.
"""

"""
반복 {m,n}
ca{2}t : a가 딱 2번이라는 뜻. caat만 매치.
ca{2,5}t : a가 2~5일 때매치된다는 뜻. caat ~ caaaaat와 매치.
"""

"""
반복 ?
ca?t : a가 0번 혹은 1번이라는 뜻. ct, cat와 매치.
ca{0,1}t 와 같은 표현이다.
"""