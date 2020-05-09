import pyaudio

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
    except KeyboardInterrupt:
        break

stream.stop_stream()
stream.close()
stream.terminate()

print('end')