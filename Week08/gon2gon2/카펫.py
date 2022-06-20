def solution(brown, yellow):
    answer = []
    total_area = brown + yellow

    for yh in range(1, (yellow+1) // 2 + 1):

        yw, impossible = divmod(yellow, yh)
        if impossible: continue

        total_w = yw + 2
        total_h = yh + 2

        if total_w * total_h == total_area:
            return [total_w, total_h]

    return answer
