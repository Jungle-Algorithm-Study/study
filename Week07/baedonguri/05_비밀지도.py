# def modify_bit(n,bit):
#     bit_len = len(bit)
#     max_len = n
#     return (max_len-bit_len)*'0'+bit

def check(bit1, bit2):
    answer = ''
    for i in range(len(bit1)):
        if bit1[i] == '0' and bit2[i] == '0': 
            answer += ' '
        else: 
            answer += '#'
    return answer

def solution(n, arr1, arr2):
    dap = []
    for a1, a2 in zip(arr1, arr2):
        # bit1 = modify_bit(n,bin(a1)[2:])
        # bit2 = modify_bit(n,bin(a2)[2:])
        bit1 = bin(a1)[2:].zfill(n) # 주형쿤 조언
        bit2 = bin(a2)[2:].zfill(n)
        dap.append(check(bit1,bit2))
    return dap


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))




