import webbrowser


# BASIC 

def play_music():
    """Default music"""
    webbrowser.open("https://open.spotify.com")


def play_youtube_music():
    webbrowser.open("https://music.youtube.com")


def play_spotify():
    webbrowser.open("https://open.spotify.com")


# SMART SEARCH

def search_song(query: str):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}+song")


def play_spotify_search(query: str):
    webbrowser.open(f"https://open.spotify.com/search/{query}")


# MOOD BASED 

def play_lofi():
    webbrowser.open(
        "https://www.youtube.com/results?search_query=lofi+study+music+live"
    )


def play_study_music():
    webbrowser.open(
        "https://www.youtube.com/results?search_query=study+music+focus+playlist"
    )


def play_bollywood():
    webbrowser.open(
        "https://www.youtube.com/results?search_query=bollywood+hits+playlist"
    )


def play_instrumental():
    webbrowser.open(
        "https://www.youtube.com/results?search_query=instrumental+background+music"
    )
