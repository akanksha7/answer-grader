import streamlit as st
from grader import grader
import time

def frontend():

    header()

    container = st.container()

    with container:
        add_answer_button_clicked = True
        isDisabled_text = False 
        isDisabled_image = False
        isDisabled_rubric = False
        score = None
    

        col1, col2, col3 = st.columns([1, 1, 0.3])  

        with col1:
            uploaded_file = st.file_uploader(f"## **Upload answer here:**", type=['png', 'jpeg', 'jpg'], disabled=isDisabled_image, )
            if uploaded_file is not None:
                isDisabled_text = True
            
            st.write("**OR**")
            uploaded_text = st.text_area("**Paste answer here:**", disabled=isDisabled_text)
            if uploaded_text.strip() !=  "":
                isDisabled_image = True

        with col2:
            rubric = st.text_area("**Enter Rubric**", key="rubric_text", height= 260)
            

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
                    
                    progress_text = "Grading answer. Please wait.."
                    my_bar = st.progress(0, text=progress_text)

                    for percent_complete in range(100):
                        time.sleep(0.01)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    time.sleep(1)
                    
                    score = grader(uploaded_file, uploaded_text, rubric)

                    my_bar.empty()

    _ , add_answer_col, _ = st.columns([1.5,1,1])
    with add_answer_col:
        st.write("")
        st.write("")
        if st.button("Add new Answer"):
            uploaded_file = None
            uploaded_text = None
            score= None

    # Display grading result
    if score is not None:
        st.subheader("Grading Result:")
        st.write(score)
   

def header():
    header_right, _ = st.columns((2, 1))
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://mcdn.wallpapersafari.com/medium/0/8/UItQvK.jpg");
    background-size: cover;
    }
    [data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)
   
    with header_right:
        st.title("Answer Grader")

    
   

def footer():
    pass