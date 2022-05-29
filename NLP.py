import speech_recognition as sr
import zipfile
import os

print(os.listdir(r"C:\Users\Acer\Downloads\recordings"))
list_rec=os.listdir(r"C:\Users\Acer\Downloads\recordings")
for fil in list_rec:
  r = sr.Recognizer()
  print(fil)
  with sr.AudioFile(fil) as source:
    audio_text = r.listen(source)
    try:
      text = r.recognize_google(audio_text)
      print('text obtaines:')
      print(text)
    except:
      print('failure')



      # for name in f.namelist():
      #     r = sr.Recognizer()
      #     print(name)
      #     with sr.AudioFile(name) as source:
      #         audio_text = r.listen(source)
      #         try:
      #             text = r.recognize_google(audio_text)
      #             print('text obtaines:')
      #             print(text)
      #         except:
      #             print('failure')
