import tkinter as tk
import threading
import pyaudio
import wave
import os
import glob

class App():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    frames = []
    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='rec',command=self.startrecording)
        self.button2 = tk.Button(main, text='stop',command=self.stoprecording)

        self.button1.pack()
        self.button2.pack()

    def startrecording(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True

        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()

    def checkFile(self, filePath):
        if os.path.exists(filePath):
            numb = 1
            while True:
                newPath = "{0}_{2}{1}".format(*os.path.splitext(filePath) + (numb,))
                if os.path.exists(newPath):
                    numb += 1
                else:
                    return newPath
        return filePath

    def stoprecording(self):
        self.isrecording = False
        print('recording complete')
        #self.filename=input('the filename?'
        TARGET_DIR = str(max(glob.glob(os.path.join('interviews', '*/')), key=os.path.getmtime))[:-1]
        self.fn = TARGET_DIR + "/response" + ".wav"
        #self.checkFile(self.filename))
        #os.makedirs(os.path.dirname(self.checkFile(self.filename)), exist_ok=True)
        self.filename = self.checkFile(self.fn)
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        main.destroy()
    def record(self):

        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)



if __name__ == "__main__":
    main = tk.Tk()
    main.title('recorder')
    main.geometry('200x50')
    app = App(main)
    main.mainloop()
