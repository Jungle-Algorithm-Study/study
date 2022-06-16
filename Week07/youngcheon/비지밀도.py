def solution(n, arr1, arr2):
    답 = []
    for i,j in zip(arr1, arr2):
        답.append(bin(i|j)[2:].zfill(n).replace('1','#').replace('0',' '))
    return 답