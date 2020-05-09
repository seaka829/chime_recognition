import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT      = pyaudio.paInt16
CHANNELS    = 1         # maxInputChannels
RATE        = 48000     # defaultSampleRate
CHUNK       = 1024
IDINDEX     = 2         # index

count = 0
x = []
y = []

audio = pyaudio.PyAudio()
stream = audio.open(
     format = FORMAT
    ,channels = CHANNELS
    ,rate = RATE
    ,frames_per_buffer=CHUNK
    ,input=True
    ,output=False
)

while stream.is_active():
    try:
        input = stream.read(CHUNK, exception_on_overflow=False)
        ndarray = np.frombuffer(input, dtype='int16')
        for i in ndarray:
            count = count + 1
            data = i.item()
            seconds = count/RATE    # 経過時間を取得
            x.append(seconds)
            y.append(data)
            # print(seconds, data)
    except KeyboardInterrupt:
        break

plt.plot(x, y)
plt.show()

stream.stop_stream()
stream.close()
stream.terminate()