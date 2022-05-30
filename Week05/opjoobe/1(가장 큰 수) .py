# 아직 notsol..... 60/100

def solution(numbers):
    answer = ''
    for i in range(9,-1,-1):
        start_with_i_list = [str(num) for num in numbers if str(num)[0]==str(i)]
        if not start_with_i_list:
            continue
        start_with_i_list.sort(key = lambda x: ((x*4)[0], (x*4)[1], (x*4)[2], (x*4)[3]))
        answer += str(int(''.join(start_with_i_list[::-1])))
    return answer


# # 가장 큰 수 #6시35분 시작 #7시5분중단 # 아직 notsol

# def special_sort(numbers):
#     numbers = list(map(str, numbers ))
#     numbers.sort(key = lambda x: (x.rjust(3,x[-1])[0], x.rjust(3,x[-1])[1], x.rjust(3,x[-1])[2]))
#     return str(int(''.join(numbers[::-1])))

# def solution(numbers):
#     answer = ''
#     # 힙으로? [0번째인덱스, 전체숫자?]
#     for i in range(9,-1,-1):
#         start_with_i_list = [str(num) for num in numbers if str(num)[0]==str(i)]
#         if not start_with_i_list:
#             continue
#         i = str(i)
#         oneflag,twoflag = False,False
#         try:
#             oneidx = start_with_i_list.index(i)
#         except:
#             oneidx = -1
#         if oneidx >= 0:
#             start_with_i_list[oneidx] = i*3
#             oneflag = True
#         try:
#             twoidx = start_with_i_list.index(i*2)
#         except:
#             twoidx = -1
#         if twoidx >= 0:
#             start_with_i_list[twoidx] = i*3
#             twoflag = True

#         start_with_i_list.sort(reverse=True)
#         if oneflag:
#             start_with_i_list[start_with_i_list.index(i*3)] = i
#         if twoflag:
#             start_with_i_list[start_with_i_list.index(i*3)] = i*2
#         answer += ''.join(start_with_i_list)
        
#     return answer

# def solution2(numbers):
#     answer = ''
#     # 힙으로? [0번째인덱스, 전체숫자?]
#     for i in range(9,-1,-1):
#         start_with_i_list = [str(num) for num in numbers if str(num)[0]==str(i)]
#         if not start_with_i_list:
#             continue
#         start_with_i_list.sort(key = lambda x: (x.rjust(3,x[-1])[0], x.rjust(3,x[-1])[1], x.rjust(3,x[-1])[2], -len(x)))
#         answer += str(int(''.join(start_with_i_list[::-1])))
#     return answer


# def solution3(numbers):
#     answer = ''
#     # 힙으로? [0번째인덱스, 전체숫자?]
#     for i in range(9,-1,-1):
#         start_with_i_list = [str(num) for num in numbers if str(num)[0]==str(i)]
#         if not start_with_i_list:
#             continue
#         start_with_i_list.sort(key = lambda x: (x*3[0], x*3[1], x*3[2], x*3[3]))
#         answer += str(int(''.join(start_with_i_list[::-1])))
#     return answer

# # print('97'<'91')
# # print('98'>'952')

# numbers = [101, 10, 232, 23]
# numbers = [1, 11, 110, 1000]
# numbers = [9,998]
# numbers = [100,1000]
# # numbers =  [104, 1]
# # numbers = [0,0,0]
# # print(solution(numbers))
# # print(solution2(numbers))

# # print('1'.rjust(4,'1'))
# # print('104'.rjust(4,'1'))

# # numbers.sort(key=lambda x: str(x)[0])
# # print(numbers[::-1])

# def solution(numbers):
#     answer = ''
#     for i in range(9,-1,-1):
#         start_with_i_list = [str(num) for num in numbers if str(num)[0]==str(i)]
#         if not start_with_i_list:
#             continue
#         print(start_with_i_list)
#         start_with_i_list.sort(key = lambda x: x*3[0])
#         answer += str(int(''.join(start_with_i_list[::-1])))
#     return answer

# # print(solution(numbers))

# # 32
# # 323

# # 32 322
# # 322 32

numbers = [100,1000]
def solution4(numbers):
    answer = ''
    for i in range(9,-1,-1):
        start_with_i_list = [str(num) for num in numbers if str(num)[0]==str(i)]
        if not start_with_i_list:
            continue
        start_with_i_list.sort(key = lambda x: ((x*4)[0], (x*4)[1], (x*4)[2], (x*4)[3]))
        answer += str(int(''.join(start_with_i_list[::-1])))
    return answer

print(solution4(numbers))