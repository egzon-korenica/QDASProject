import playsound
import os
from pathlib import Path

    
directory = './audio'    
counter = 0
for filename in os.listdir(directory):
    txt = input("Next question or repeat? n or r: ")
    if txt == "n":
              fname = "0" + str(counter) + ".mp3"
              print(fname)
              playsound.playsound("./audio/" + fname, True)
              response = input("share your thoughts: ")
              with open("response.txt", "a") as f: 
                f.write(response)
                f.write("\n")
                f.close()
    counter +=1 

        
      

