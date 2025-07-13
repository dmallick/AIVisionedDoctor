#Comments: This script is designed to handle disease identification using visual modal (using image) by a pre-trained model.
# It take an image of a skin condition and provides a detailed medical analysis.
# The input is an image file and a query, and the output is a text response containing the analysis.
# The script uses the Groq API to interact with the model and generate the response.
# 
# 
# 
# 
# 
# 
# 
# 
# ###
import os
import base64
from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS

load_dotenv()
def analyze_image_with_query(query, encoded_image, model):
    """
    Analyzes an image with a query using a specified model.
    
    :param query: The query to analyze the image.
    :param encoded_image: Base64 encoded string of the image.
    :param model: The model to use for analysis.
    :return: Analysis response from the model.
    """
    groq_client = Groq(api_key=os.environ.get('GROQ_API_KEY'))
    
    message = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    
    chat = groq_client.chat.completions.create(model=model, messages=message)
    return chat.choices[0].message.content
def encode_image(image_path):
    """
    Encodes an image file to base64 format.
    
    :param image_path: Path to the image file.
    :return: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

GROQ_API_KEY=os.environ.get('GROQ_API_KEY')


image_path = '/Users/debasishmallick/workspace/AIVisionedDoctor/acne.png'
with open(image_path, "rb") as image_file:
    encoded_base64_image = base64.b64encode(image_file.read()).decode('utf-8')


groq_client = Groq(api_key=GROQ_API_KEY)
model = "meta-llama/llama-4-scout-17b-16e-instruct"
message  = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Analyze the following image of a skin condition and provide a detailed medical analysis."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{encoded_base64_image}"
                }
            }
        ]
    }   

]

chat = groq_client.chat.completions.create(model=model, messages=message)

print("Step 2: " + chat.choices[0].message.content)

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


#input_text="Hi this is Ai with Hassan!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")