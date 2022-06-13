def change_note(note):
    note = note.replace('C#','c')
    note = note.replace('D#','d')
    note = note.replace('F#','f')
    note = note.replace('G#','g')
    note = note.replace('A#','a')
    return note

def solution(m, musicinfos):
    m = change_note(m)
    answer = []
    for i in musicinfos:
        info = list(i.split(','))
        sm,ss = map(int,info[0].split(':'))
        em,es = map(int,info[1].split(':'))
        
        if sm <= em and ss <= es:
            time = (em-sm)*60+(es-ss)
        else:
            # 예를들면 11:59 부터 12:01 까지라면 60에 59를 빼서 1을 더하는 식으로
            time = (em-sm)*60-ss+es
        
        title = info[2]
        note = change_note(info[3])
        
        if len(note) < time:
            # 계산 귀찮아서 걍 1000배 하고 자름.. 효율성은 똥망임
            note = (note*1000)[:time]
        else:
            note = note[:time]
        
        if m in note:
            answer.append([title, note])
    
    if answer:
        # 음계 길이만큼 소트하고 거꾸로 뒤집음 (긴 것 먼저 나오게)
        answer.sort(key = lambda x: len(x[1]), reverse = True)
        return answer[0][0]
    else:
        return "(None)"

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", 
                          "13:00,13:05,WORLD,ABCDEF"]))