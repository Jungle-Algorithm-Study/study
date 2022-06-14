def solution(m, musicinfos):
    answer = ''
    n = m.replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
    d = []
    for i in musicinfos :
        a = i.split(',')
        b = a[0].split(':')
        c = a[1].split(':')
        second = (int(c[0])*60 + int(c[1])) - (int(b[0])*60 + int(b[1]))
        print(second)
        score = a[3].replace('C#','H').replace('D#','I').replace('F#','J').replace('G#','K').replace('A#','L')
        len_score = len(score)
        
        mul = second // len_score + 1 
        score = score * mul
        score = score[:second]
        
        if n in score :
            d.append([second,a[2]])
            
    if not d :
        return "(None)"
    
    return sorted(d,key=lambda x : x[0], reverse=True)[0][1]
