from openai import OpenAI
from api import api

my_api_key = api()

def transcribe():
    client = OpenAI(api_key=my_api_key)
    audio_file = open("output.wav", "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    transcript = transcript[:-10]
    # print(transcript)
    file_path = "transcription.txt"
    with open(file_path, 'w') as file:
        file.write(transcript)