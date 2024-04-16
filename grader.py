import google.generativeai as genai
from config import GENAI_API_KEY
import PIL.Image

def grader(uploaded_file, uploaded_text, rubric):
    genai.configure(api_key=GENAI_API_KEY)
    
    if uploaded_file is not None:
        img_model = genai.GenerativeModel('gemini-pro-vision')
        img = PIL.Image.open(uploaded_file)
        response = img_model.generate_content(["Grab the text from the image.", img], stream=True)
        response.resolve()
        student_answer = response.text
    elif uploaded_text is not None:
        student_answer = uploaded_text

    text_model = genai.GenerativeModel(
        'gemini-pro',
        generation_config=genai.GenerationConfig(
            temperature=0.1,
    ))

    prompt = f"""Use the provided question\'s rubric to give a score for the following answer. Also provide reason for the score.

    <RUBRIC>: {rubric}
    <ANSWER>: {student_answer}

    Output should be of the format: 
    <SCORE>: score
    """
    response = text_model.generate_content([prompt], stream=True)
    response.resolve()
    score = response.text
    
    return score