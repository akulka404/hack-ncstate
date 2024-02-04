import pyaudio
import wave

def recordAudio():
    # Audio recording parameters
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100              # Sample rate
    CHUNK = 1024              # Frames per buffer
    RECORD_SECONDS = 30       # Recording time in seconds
    WAVE_OUTPUT_FILENAME = "output.wav"  # Output filename

    # Initialize pyaudio
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()