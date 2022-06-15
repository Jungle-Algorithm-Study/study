def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2) :
        arr = str(bin(a | b)[2:].zfill(n))
        answer.append(arr.replace('1', '#').replace('0', ' '))

    return answer
