def change_note(note):
    note = note.replace('C#','c')
    note = note.replace('D#','d')
    note = note.replace('F#','f')
    note = note.replace('G#','g')
    note = note.replace('A#','a')
    return note

def solution(m, musicinfos):
    m = change_note(m)
    answer = [["(None)",""]]
    
    for i in musicinfos:
        info = list(i.split(','))
        sm,ss = map(int,info[0].split(':'))
        em,es = map(int,info[1].split(':'))
        
        time = (em*60+es)-(sm*60+ss)
        
        title = info[2]
        note = change_note(info[3])
        
        # 계산 귀찮아서 걍 1000배 하고 자름.. 효율성은 똥망임
        note = (note*1000)[:time]
        
        if m in note:
            answer.append([title, note])
    
    # 길이 sort
    answer.sort(key = lambda x: len(x[1]), reverse = True)
    return answer[0][0]