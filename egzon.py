import playsound
import os

'''    
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

TARGET_DIR = "interviews/person"
n = 1

while os.path.isdir(path):
        path = os.path.join(TARGET_DIR + str(n))
      n+=1
      print(str(n))
      os.mkdir(path) 

'''
import os


import os, glob

'''
print(str(max(glob.glob(os.path.join('interviews', '*/')), key=os.path.getmtime)))

foldername = str(max(glob.glob(os.path.join('interviews', '*/')), key=os.path.getmtime))[:-1]

def checkPath(filePath):
        if os.path.exists(filePath):
            numb = 1
            while True:
                newPath = "{0}_{2}{1}".format(*os.path.splitext(filePath) + (numb,))
                if os.path.exists(newPath):
                    numb += 1
                else:
                    return newPath
        return filePath


print(checkPath(foldername))

os.mkdir(checkPath(foldername))





import os
i=1
keepGoing=True
while keepGoing:
  path = "interviews/interview_{}/".format(i)
  if not os.path.exists(path):
    os.makedirs(os.path.dirname("interviews/interview_{}/".format(i)), exist_ok=False)
    keepGoing = False
  i += 1

'''


foldername = str(max(glob.glob(os.path.join('interviews', '*/')), key=os.path.getmtime))[:-1]

print(foldername)
