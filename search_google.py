import pywhatkit
from Head.Mouth import speak
from Data.dlg_data.dlg import *
import random

def search_google(text):
    dlg = random.choice(search_result)
    pywhatkit.search(text)
    speak(dlg)


