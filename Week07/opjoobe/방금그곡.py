#방금그곡 # 7시 4분 시작 # 몇분걸렸는진 까먹음 # 문제조건을 잘읽자
def lyric_transform(l):
    l = l.replace('C#','c')
    l = l.replace('D#','d')
    l = l.replace('F#','f')
    l = l.replace('G#','g')
    l = l.replace('A#','a')
    return l
    
def play_min(s,e):
    s_hour, s_min = s.split(':')
    e_hour, e_min = e.split(':')
    s_total_min = int(s_hour)*60 + int(s_min)
    e_total_min = int(e_hour)*60 + int(e_min)
    return e_total_min - s_total_min
    
def solution(m, musicinfos):
    answer = ''
    answer_max_len = 0
    new_m = lyric_transform(m)

    for music in musicinfos:
        start, end, title, lyric = music.split(',')
        play_len = play_min(start, end)
        new_lyric = lyric_transform(lyric)
        music_len = len(new_lyric)
        rep, rest = divmod(play_len, music_len)
        total_lyric = new_lyric * rep + new_lyric[:rest]
        
        if new_m in total_lyric:
            if not answer:
                answer = title
                answer_max_len = play_len
            else:
                if answer_max_len < play_len:
                    answer_max_len = play_len
                    answer = title
    if not answer:
        answer = "(None)"
    
    return answer