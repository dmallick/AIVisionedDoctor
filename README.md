# AIVisionedDoctor
This a AI model impersonating as doctor. The user will share an image and ask using his voice about the problem. This is the same way, how you tell doctor in the hospital. Now, the AI would repond to you in the voice itself.

There are 3 main key players. One is the patient (human), the other one would AI acting as doctor. Finaaly the 3rd one is the technologies which bridge between doctor and patient.

ENVIRONMENT:
1. GROQ: [Visit GROQ](https://console.groq.com/home) 
    GROQ is an AI inference company. It runs LLMs in it's environment and exposes SDKs through which you can query the LLMs
2. Llama 4 multimodal acting as Doctor
3. Tools and Technologies and usage
    Python              Core Language
    GROK                SDK to access LLM running in GROK Infrastructure
    Whisper             OpenAI LLM Convert Speech to Text(Transcript)
    ffmpeg              Used for converting, encoding, decoding, and streaming multimedia
    portaudio           Used for Accessing microphone or speaker and Recording raw audio
    SpeechRecognition   speech-to-text
    gTTS                written text into spoken audio
    Gradio              UI
    VS Code             Development IDE 

Functional Flow:
1. The patient uploads the photo of the disease (assume we can visualize it like Acne) and tells in details about it using mike.
2. The Doctor sees the picture and the audio descrption of the problem and then respond with the disease detection and respond in audio

Major Components:
1. Voice Recorder: Records patient's voice recording
2. VoiceToText Converter: Converts patient's voice to text transcript. To be passed as a parameter to LLM.
3. Image Uploader: Visual description of the disease to be sent to LLM along with transcript of patient's audio
4. TextToAudio: LLM will respond in text. This needs to be converted to audio to be delivered to patient


