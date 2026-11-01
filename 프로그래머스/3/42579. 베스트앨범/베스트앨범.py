def solution(genres, plays):
    answer = []
    # 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
    genre_total = {} # { "classic": 1450,"pop": 3100}
    genre_songs = {} # { "classic": [[500, 0], [150, 2], [800, 3]] }
    
    for i in range(len(genres)):
        if genres[i] not in genre_total:
            genre_total[genres[i]] = plays[i]
        else:
            genre_total[genres[i]] += plays[i]
        if genres[i] not in genre_songs:
            genre_songs[genres[i]] = [[plays[i], i]]
        else:
            genre_songs[genres[i]].append([plays[i], i])

    total_items = list(genre_total.items())
    total_items.sort(key=lambda x:x[1], reverse=True)
    
    for item in total_items:

        genre = item[0]
        genre_songs[genre].sort(key=lambda x:x[0], reverse=True)

        for i in range(len(genre_songs[genre])):
            if i >=2:
                break
            answer.append(genre_songs[genre][i][1])
                
        
    return answer