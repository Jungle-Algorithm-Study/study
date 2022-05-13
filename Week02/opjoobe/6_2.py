# sol
def solution(files):
    answer = []
    new_files = []
    head, number = '',''
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for j in range(len(number)):
                    if not number[j].isdigit():
                        number = number[:j]
                        break
                new_files.append([head, number, file])
                break
    new_files.sort(key= lambda x: (x[0].lower(),int(x[1])))
    answer = [x[2] for x in new_files]
    return answer

# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "foo010bar020.zip"]
# files = ['muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT','F15']
print(solution(files))