def calc_min(start, end):
    
    start_hour, start_minute = map(int,start.split(':'))
    end_hour, end_minute = map(int,end.split(':'))
    hour = end_hour - start_hour
    minute = end_minute - start_minute
    
    if minute < 0:
        hour -= 1
        minute += 60
    minute += 60*hour
    
    return minute

convert = lambda m: m.replace('G#','a').replace('C#','b').replace("D#",'c').replace("F#",'d').replace("A#",'e')



def solution(m, musicinfos):
    answer = []
    
    m = convert(m)
    n = len(m)
    
    for info in musicinfos:
        start, end, title, score = info.split(',')
        minute = calc_min(start, end)
        
        score = convert(score)
        
        full_score = score * (minute//len(score) + 1)
        full_score = full_score[:minute]
        
        if m in full_score:
            answer.append([minute, title])
        
        
    return "(None)" if not answer else sorted(answer, reverse=True, key=lambda x:x[0])[0][1]
