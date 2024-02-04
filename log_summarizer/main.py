from logger import logger
from recordAudio import recordAudio
from transcribe import transcribe
import sys

recordAudio()
transcribe()
cmd = str(sys.argv[1])
logger(cmd)