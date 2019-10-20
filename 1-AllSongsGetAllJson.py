import lyricsgenius

songCnt = 100
sortV = "popularity"  # use title or popularity
geniusKey = ""

# ----
genius = lyricsgenius.Genius(
    geniusKey)
artist = genius.search_artist("Money Boy", max_songs=songCnt, sort=sortV)
print(artist.songs)
artist.save_lyrics()
