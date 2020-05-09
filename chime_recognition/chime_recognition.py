import pyaudio
import numpy as np

FORMAT      = pyaudio.paInt16
CHANNELS    = 1
RATE        = 48000
CHUNK       = 1024
IDINDEX     = 2

audio = pyaudio.PyAudio()

stream = audio.open(
    format = FORMAT
    ,channels = CHANNELS
    ,rate = RATE
    ,frames_per_buffer=CHUNK
    ,input=True
    ,output=False
)

print('start')

while stream.is_active():
    try:
        input = stream.read(CHUNK, exception_on_overflow=False)
        ndarray = np.frombuffer(input, dtype='int16')
        for i in range(len(ndarray)):
            data = np.asscalar(ndarray[i])
            print(i, data)
    except KeyboardInterrupt:
        break

print('end')

stream.stop_stream()
stream.close()
stream.terminate()