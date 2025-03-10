
from gtts import gTTS

from playsound import playsound

flag = 'Hello Lucy!'

language = 'en'

myobj = gTTS(text=flag, lang=language, slow=False)

myobj.save("flag.mp3")

playsound('flag.mp3')