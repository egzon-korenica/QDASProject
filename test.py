import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611) 
 
 
 
def record(self):
        try:
            with sf.SoundFile(self.filepath,
                                       mode='x', samplerate=self.SAMPLE_RATE,
                                       channels=self.CHANNELS, subtype=None) as file:
                with sd.InputStream(samplerate=self.SAMPLE_RATE, device=self.mic_id,
                                           channels=self.CHANNELS, callback=self.callback):
                    logger.info(f"New recording started: {self.sound_file.name}")
                    try:
                        while True:
                            file.write(self.mic_queue.get())

                    except RuntimeError as re:
                        logger.debug(f"{re}. If recording was stopped by the user, then this can be ignored")

record()
