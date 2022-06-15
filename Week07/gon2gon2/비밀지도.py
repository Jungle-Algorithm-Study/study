convert = lambda x,n: x[2:].rjust(n,'0')

def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        
        row = convert(bin(a1|a2), n)
        x = row.replace('1','#').replace('0',' ')
        answer.append(x)
    
    return answer

# 영천st.
solution = lambda n, arr1, arr2: [bin(a1|a2)[2:].rjust(n, '0').replace('1','#').replace('0',' ') for a1, a2 in zip(arr1, arr2)]
