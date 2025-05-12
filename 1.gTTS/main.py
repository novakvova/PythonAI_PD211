from gtts import gTTS
import os

text = "Вчимо програмування і насолоджуємося цим процесом. ;)"

tts = gTTS(text=text, lang='uk')
tts.save('my.mp3')

os.system("start my.mp3")