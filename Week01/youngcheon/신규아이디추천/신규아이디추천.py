def three(s):
    if '..' in s: 
        s=s.replace('..','.')
    else: 
        return s
    return three(s)

def seven(s):
    if len(s)<=2:
        s += s[-1]
    else:
        return s
    return seven(s)

def solution(new_id):
    #1
    answer = new_id.lower()
    #2
    answer = ''.join(list(map(lambda x: x if x.islower() or x.isdigit() or x in ['-','_','.'] else '', answer)))
    #3
    answer = three(answer)
    #4
    answer = answer.strip('.')
    #5
    answer = answer if answer else 'a'
    #6
    answer = answer[:15] if len(answer)>=15 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    #7
    answer = seven(answer)
    return answer