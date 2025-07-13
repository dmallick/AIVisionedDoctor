#comments: 
# This script is designed to handle patient voice recognition using a pre-trained model.
# It takes an audio file as input and provides a text transcription of the spoken words.
# The input is an audio file, and the output is a text response containing the transcription.
# The script uses the SpeechRecognition library to interact with the audio file and generate the transcription.
# 
#  pip3 install speechrecognition
#  pip3 install pydub
# 
# 
# #

import speech_recognition as sr
from pydub import AudioSegment
from dotenv import load_dotenv
from pydub.playback import play
from io import BytesIO
from groq import Groq
import logging
import os


load_dotenv()
#Recognizes speech from an audio file and returns the transcription.
def recognize_speech_from_audio(audio_file_path):
    """
    
    
    :param audio_file_path: Path to the audio file.
    :return: Transcription of the audio.
    """
    recognizer = sr.Recognizer()
    
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)
    
    # Play the audio file
    play(audio)
    
    # Convert audio to a format compatible with SpeechRecognition
    with BytesIO() as audio_buffer:
        audio.export(audio_buffer, format="wav")
        audio_buffer.seek(0)
        
        with sr.AudioFile(audio_buffer) as source:
            audio_data = recognizer.record(source)
    
    # Recognize speech using Google Web Speech API
    try:
        transcription = recognizer.recognize_google(audio_data)
        return transcription
    except sr.UnknownValueError:
        logging.error("Google Web Speech API could not understand the audio.")
        return None
    except sr.RequestError as e:
        logging.error(f"Could not request results from Google Web Speech API; {e}")
        return None


#Simplified function to record audio from the microphone and save it as an MP3 file.
def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_filepath="test_audio.mp3"
#record_audio(file_path=audio_filepath)   

# testing the function
#record_audio("test_audio.mp3")



#This function transcribes audio using the Groq API with a specified STT model.
def transcribe_with_groq(audio_filepath, GROQ_API_KEY=None):
    stt_model="whisper-large-v3"

    GROQ_API_KEY=os.environ.get('GROQ_API_KEY')
    print("Step1: transcribe_with_groq")
    #groq_client = Groq(api_key=GROQ_API_KEY)

    client=Groq(api_key=GROQ_API_KEY)
        
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )
    return transcription.text

transcription = transcribe_with_groq(audio_filepath, os.environ.get('GROQ_API_KEY'))
logging.info("Transcription completed successfully.")
print(transcription)
