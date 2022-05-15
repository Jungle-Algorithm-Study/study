# [프로그래머스] 전화번호 목록 (python)
# https://programmers.co.kr/learn/courses/30/lessons/42577

# def solution(phone_book):
#     phone_book.sort()
#     len_pb = len(phone_book)

#     for i in range(len_pb-1):
#         if len(phone_book[i]) >= len(phone_book[i+1]):
#             check = phone_book[i].startswith(phone_book[i+1])
#         else:
#             check = phone_book[i+1].startswith(phone_book[i])
        
#         if check:
#             return False
#     return True


# 고니 조언 참고
def solution(phone_book):
    phone_book.sort()
    len_pb = len(phone_book)

    for i in range(len_pb-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

        



print(solution(["12","123","1235","567","88"]))