def solution(brown, yellow):
    extent = brown + yellow  # 넓이
    
    for w in range(extent, 0, -1):
        if extent % w == 0:
            h = extent // w
            if (w-2) * (h-2) == yellow:
                return [w, h]
                break