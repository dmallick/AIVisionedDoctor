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
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.environ.get('GROQ_API_KEY')

import base64
image_path = '/Users/debasishmallick/workspace/AIVisionedDoctor/acne.png'
with open(image_path, "rb") as image_file:
    encoded_base64_image = base64.b64encode(image_file.read()).decode('utf-8')

from groq import Groq
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
#response = chat.get_response()
print(chat.choices[0].message.content)



# Below is the Output from the model. print(chat.choices[0].message.content) generates the following response:
""" Based on the provided image, here is a detailed medical analysis:

**Clinical Presentation:**
The image depicts a young male with a significant acne vulgaris presentation on his face, particularly on the cheek area.

**Key Features:**

* **Multiple comedones:** The presence of numerous comedones (blackheads and whiteheads) on the face, particularly on the cheek, suggests a diagnosis of acne vulgaris.
* **Inflammatory lesions:** The presence of multiple red, inflamed papules and pustules indicates an inflammatory component to the acne.
* **Severity:** The acne appears to be of moderate to severe severity, with a significant number of lesions and some clustering.

**Differential Diagnosis:**

* **Acne vulgaris:** This is the most likely diagnosis, given the presence of comedones, inflammatory lesions, and the typical distribution on the face.
* **Other conditions:** Other possible differential diagnoses could include:
        + Rosacea: characterized by flushing, telangiectasias, and papules, but typically spares the comedones.
        + Folliculitis: an inflammation of the hair follicles, which could present with similar lesions, but often with a more acute onset.

**Pathophysiology:**
Acne vulgaris is a multifactorial disorder involving:

* **Sebum production:** Increased sebum production leads to clogged pores.
* **Comedone formation:** Clogged pores lead to comedone formation.
* **Inflammation:** Bacterial colonization (e.g., Propionibacterium acnes) and inflammation contribute to the development of inflammatory lesions.

**Treatment Options:**
Treatment for acne vulgaris typically involves a combination of:

* **Topical retinoids:** To prevent comedone formation and promote skin turnover.
* **Benzoyl peroxide:** To reduce bacterial colonization and inflammation.
* **Antibiotics:** Oral or topical antibiotics to target inflammatory lesions.
* **Hormonal therapies:** For females, hormonal treatments may be considered to regulate sebum production.

**Recommendations:**

* **Dermatological evaluation:** A thorough dermatological evaluation is recommended to confirm the diagnosis and assess the severity of the acne.
* **Treatment plan:** A personalized treatment plan should be developed, taking into account the individual's skin type, medical history, and treatment goals.
* **Follow-up:** Regular follow-up appointments are essential to monitor treatment efficacy and adjust the treatment plan as needed.
 """

