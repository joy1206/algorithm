def solution(wallpaper):
    lux = 21e8
    luy = 21e8
    rdx = -21e8
    rdy = -21e8
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    answer = [lux, luy, rdx+1, rdy+1]
    return answer