'''
어떤 번호가 다른 번호의 접두어인 경우...
원소가 문자열인 리스트는 정렬하면 접두사를 기준으로 정렬된다.
따라서 앞뒤만 비교하면 된다.
'''

def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return True
