def solution(m, musicinfos):
    answer = ''
    songs = []
    maxrun = -1
    m = m.replace('C#','c').replace('D#', 'd').replace('F#','f').replace('G#','g').replace('A#', 'a')
    
    for music in musicinfos :
        start, end, title, sheet = music.split(',')
        sheet = sheet.replace('C#','c').replace('D#', 'd').replace('F#','f').replace('G#','g').replace('A#', 'a')
        long = len(sheet)
        
        sh, sm = map(int,start.split(':')) # start hour, start min
        eh, em = map(int,end.split(':')) # end hour, end min
        running = (eh - sh) * 60 + (em - sm) # running min 
        
        song = (sheet * (running // long)) + sheet[:(running % long)] # full sheet
        songs.append((title, running, song))
    
    for music in songs :
        title, running, song = music
        if m in song and running > maxrun: 
            answer = title
            maxrun = running
    
    return answer if maxrun > 0 else "(None)"
