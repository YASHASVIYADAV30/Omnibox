import webbrowser

# basic open
def open_google():
    webbrowser.open("https://google.com")


def open_youtube():
    webbrowser.open("https://youtube.com")


def open_gmail():
    webbrowser.open("https://mail.google.com")


def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com")


def open_spotify():
    webbrowser.open("https://open.spotify.com")


def open_github():
    webbrowser.open("https://github.com")


def open_chatgpt():
    webbrowser.open("https://chat.openai.com")


def open_linkedin():
    webbrowser.open("https://linkedin.com")


def open_stackoverflow():
    webbrowser.open("https://stackoverflow.com")


#SEARCH 

def search_google(query: str):
    webbrowser.open(f"https://www.google.com/search?q={query}")


def search_youtube(query: str):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def search_github(query: str):
    webbrowser.open(f"https://github.com/search?q={query}")


# MULTI TABS 

def open_study_tabs():
    sites = [
        "https://youtube.com",
        "https://stackoverflow.com",
        "https://github.com",
        "https://chat.openai.com"
    ]

    for site in sites:
        webbrowser.open_new_tab(site)
