def remove_2dots(some_text):
    
    if '..' in some_text:
        some_text = some_text.replace('..', '.')
        return remove_2dots(some_text)
    
    return some_text
    
    


def solution(new_id):
    # 1단계, 모두 소문자로 변환
    new_id = new_id.lower()
    
    # 2단계
    # 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    temp_id = ''
    for char in new_id:
        if char.islower() or char.isdigit() or char in ['-','_','.']:
            temp_id += char
    new_id = temp_id
    
    # 3단계 연속된 점 두개를 하나로 바꿔줍니다
    new_id = remove_2dots(new_id)
    print('3단계: ', new_id)
    # 4단계
    # 맨 앞이나 뒤가 .이면 제거합니다
    new_id = new_id[1:] if new_id[0] == '.' else new_id
    if new_id:
        new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    else:
        # 5단계
        # 빈 문자열이라면 a를 대입합니다.
        new_id = 'a'
        
    # 6단계
    # 16자 이상이면 15개까지만
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    # 7단계
    while len(new_id) <=2:
        new_id += new_id[-1]

    return new_id
