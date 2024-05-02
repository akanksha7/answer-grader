import google.generativeai as genai
from config import GENAI_API_KEY
import PIL.Image
import constants

def grader(uploaded_files, uploaded_text, rubric, marking_type):
    genai.configure(api_key=GENAI_API_KEY)
    
    if uploaded_files:
        img_model = genai.GenerativeModel('gemini-pro-vision')
        img = PIL.Image.open(uploaded_files)
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

    if marking_type == constants.LENIENT:
        prompt = f"""Use the provided question\'s rubric to give a score for the following answer. Ensure that you don't induce your own bias, judge solely on the basis of the rubric. Do very lenient marking.

        <RUBRIC>: {rubric}
        <ANSWER>: {student_answer}
        """
    elif marking_type == constants.STRICT:
        prompt = f"""Use the provided question\'s rubric to give a score for the following answer. Ensure that you don't induce your own bias, judge solely on the basis of the rubric. Do very strict marking.

        <RUBRIC>: {rubric}
        <ANSWER>: {student_answer}
        """
    
    else:
        prompt = f"""Use the provided question\'s rubric to give a score for the following answer. Ensure that you don't induce your own bias, judge solely on the basis of the rubric. 

        <RUBRIC>: {rubric}
        <ANSWER>: {student_answer}
        """
    
    response = text_model.generate_content([prompt], stream=True)
    response.resolve()
    score = response.text
    
    return score