import playsound


txt = input("Are you ready? y or n: ")

if txt == 'y':
    playsound.playsound('./covid.mp3', True)
else:
    exit()
