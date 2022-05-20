# 성곤쓰 풀이참고, 처음에는 이중포문돌림 
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
