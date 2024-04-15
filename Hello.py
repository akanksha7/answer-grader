import streamlit as st
from streamlit.logger import get_logger
import google.generativeai as genai

genai.configure(api_key="AIzaSyBN6_iW25NEfLLxScsDThFDJm6F3evMPb0")
import PIL.Image

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Answer Grader",
        layout='wide'
    )

    # Header section
    header_right, _ = st.columns((2, 1))
    with header_right:
        st.title("Answer Grader")

    container = st.container()

    with container:
        add_answer_button_clicked = True
        isDisabled_text = False 
        isDisabled_image = False
        isDisabled_rubric = False
        score = None
    

        col1, col2, col3 = st.columns([1, 1, 0.3])  

        with col1:
            uploaded_file = st.file_uploader(f"Upload answer here:", type=['png', 'jpeg', 'jpg'], disabled=isDisabled_image, )
            if uploaded_file is not None:
                isDisabled_text = True
            
            st.write("OR")
            uploaded_text = st.text_area("paste answer here:", disabled=isDisabled_text)
            if uploaded_text.strip() !=  "":
                isDisabled_image = True

        with col2:
            rubric = st.text_area("Enter Rubric", key="text", height= 260)
            

        with col3:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            grade_button = st.button(f"Grade Answer", type='primary')
            if grade_button:
                if rubric.strip() == "":
                    st.warning("Please add rubric.")
                elif uploaded_file is None and not(isDisabled_image):
                    st.warning("Please add answer.")
                else:
                    score = grade(uploaded_file, uploaded_text, rubric)

    _ , add_answer_col, _ = st.columns([1.5,1,1])
    with add_answer_col:
        if st.button("Add new Answer"):
            uploaded_file = None
            uploaded_text = None
            rubric = None
            score= None
    # Display grading result
    if score is not None:
        st.subheader("Grading Result:")
        st.write(score)
   

def grade(uploaded_file, uploaded_text, rubric):
    
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

if __name__ == "__main__":
    run()
