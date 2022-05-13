import re
def solution(files):
    answer = []
    new_files = []
    files_length = len(files)
    head, number, tail = '','',''
    for i in range(files_length):
        file = files[i]
        line = ''.join([str(int(x.isdigit())) for x in file])
        print(file)
        print(line)
        num_idx = line.find('1')
        tail_idx = num_idx + line[num_idx:].find('0')
        if not tail_idx:
            tail_idx = files_length
        print(num_idx, tail_idx)
        head = file[:num_idx].lower()
        number = int(file[num_idx:tail_idx])
        tail = file[tail_idx:]
        new_files.append([head, file, number])
    print(new_files)
    new_files.sort(key= lambda x: (x[0],x[2]))
    answer = [x[1] for x in new_files]
    return answer

# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "foo010bar020.zip"]
# files = ['muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT','F15']
print(solution(files))