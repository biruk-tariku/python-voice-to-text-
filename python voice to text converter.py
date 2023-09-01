import speech_recognition as sr

audio_file = "hello_there.mp3"

r= sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio_data = r.record(source)

text = r.recognize_google(audio_data)

with open("output.txt", "w") as f:
    f:write(text)