from collections import Counter, defaultdict


def solution(genres, plays):
    genre_totalPlays = Counter()
    genre_songs = defaultdict(list)

    for i, genre in enumerate(genres):
        genre_totalPlays[genre] += plays[i]
        genre_songs[genre].append(i)

    for song in genre_songs.values():
        song.sort(key=lambda x: -plays[x])

    answer = []
    for genre, _ in genre_totalPlays.most_common():
        answer.extend(genre_songs[genre][:2])
    return answer
