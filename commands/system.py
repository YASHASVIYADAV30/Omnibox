import os
import subprocess
import webbrowser
from pathlib import Path


# BASIC APPS 

def open_notepad():
    os.system("notepad")


def open_calculator():
    os.system("calc")


def open_chrome():
    webbrowser.open("https://google.com")


def open_vscode():
    os.system("code .")


# FOLDERS 

def open_downloads():
    downloads = str(Path.home() / "Downloads")
    os.startfile(downloads)


def open_documents():
    documents = str(Path.home() / "Documents")
    os.startfile(documents)


def open_desktop():
    import os
    os.system("explorer shell:desktop")





# POWER CONTROL 

def shutdown_pc():
    os.system("shutdown /s /t 1")


def restart_pc():
    os.system("shutdown /r /t 1")


def lock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")


# UTILITIES 

def take_screenshot():
    try:
        import pyautogui
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
    except:
        pass


def open_task_manager():
    subprocess.Popen("taskmgr")
