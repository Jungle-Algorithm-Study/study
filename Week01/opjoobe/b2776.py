# #백준 #2776 # 암기왕 #5월5일 오전7시42분
# import sys, collections
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     note1 = list(map(int, (input().strip().split())))
#     M = int(input())
#     note2 = list(map(int, (input().strip().split())))
#     note1hash = collections.defaultdict()
#     for num in note1:
#         note1hash[num] = 1

#     for num in note2:
#         if num in note1hash:
#             print(1)
#         else:
#             print(0)

#백준 #2776 # 암기왕 #5월5일 오전8시5분
import sys, collections
input = sys.stdin.readline

def BS(arr, s, e, n):
    while s <= e:
        m = (s+e)//2
        case = arr[m]
        if case == n:
            return 1
        elif case < n:
            s = m+1
        else:
            e = m-1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = sorted(list(map(int, (input().strip().split()))))
    M = int(input())
    note2 = list(map(int, (input().strip().split())))
    for num in note2:
        print(BS(note1, 0, N-1, num))