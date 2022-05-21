import re

def solution(phone_book):
    for i in phone_book :
        for j in phone_book :
            if re.search("^"+i,j) :
                return False
    return True
