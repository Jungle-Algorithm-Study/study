m = "CC#BCC#BCC#BCC#B"	
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

def check_time(start,end):
    start = start.split(':')
    end = end.split(':')
    h_ = int(end[0])-int(start[0])
    m_ = int(end[1])-int(start[1])

    return h_ * 60 + m_

    
def solution(m, musicinfos):
    m = m.replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
    result = []
    for musicinfo in musicinfos:
        start, end, title, note = musicinfo.split(',')
        running_time = check_time(start,end)
        edit_note = note.replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')

        if len(edit_note) <= running_time:
            x,y = divmod(running_time,len(edit_note))
            sub_string = edit_note*x + edit_note[:y]
            
            if m in sub_string:
                result.append((title,running_time))
        else:
            if m in edit_note[:running_time]:
                result.append((title,running_time))

    if not result:
        return "(None)"
    
    return sorted(result, key=lambda x:x[1], reverse=True)[0][0]

print(solution(m, musicinfos))




    


