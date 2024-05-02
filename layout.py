import streamlit as st
from grader import grader
import time
import constants

def body():
    if "file_uploader_key" not in st.session_state:
        st.session_state["file_uploader_key"] = 0
    if "text_key" not in st.session_state:
        st.session_state["text_key"] = 1

    if "uploaded_files" not in st.session_state:
        st.session_state["uploaded_files"] = []

    
    marking_style = header()
    uploaded_files = []

    container = st.container()
    
    with container:
        isDisabled_text = False 
        isDisabled_image = False
        score = None
    
       
        col1, col2, col3 = st.columns([1, 1, 0.3])  
        

        with col1:
            uploaded_files = st.file_uploader(f"## **Upload answer here:**", type=['png', 'jpeg', 'jpg'], disabled=isDisabled_image, accept_multiple_files=True, key = st.session_state["file_uploader_key"] )
            if uploaded_files:
                st.session_state["uploaded_files"] = uploaded_files
                isDisabled_text = True
            
            st.write("**OR**")
            uploaded_text = st.text_area("**Paste answer here:**", disabled=isDisabled_text, key = st.session_state["text_key"])
            if uploaded_text.strip() !=  "":
                isDisabled_image = True

        with col2:
            rubric = st.text_area("**Enter Rubric**", key="rubric_text", height= 260)


        with col3:
            for i in range(8):
                st.write("")
            
            if st.button("Add new Answer"):
                st.session_state["file_uploader_key"] += 1
                st.session_state["text_key"] += 1
                score= None
                st.rerun()
            
    _ , add_answer_col, _ = st.columns([1.5,1,1])
    with add_answer_col:
        st.write("")
        st.write("")
       
        grade_button = st.button(f"Grade Answer", type='primary')
        if grade_button:
            if rubric.strip() == "":
                st.warning("Please add rubric.")
            elif not uploaded_files and uploaded_text.strip() == "":
                st.warning("Please add answer.")
            else:
                
                progress_text = "Grading answer. Please wait.."
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.05)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                
                try:
                    score = grader(uploaded_files, uploaded_text, rubric, marking_style)
                except:
                    st.error("Error while grading")
                    

                my_bar.empty()


    # Display grading result
    if score is not None:
        st.subheader("Grading Result:")
        st.write(score)
   

def header():
    
    header_left, _ , header_right= st.columns((2, 1, 0.5))

    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{

    background-image: url("https://img.freepik.com/free-vector/eye-catching-glowing-question-mark-sign-background-who-why-query-vector_1017-48020.jpg?w=1060&t=st=1714678379~exp=1714678979~hmac=cf187d978d7b53500e3d53cb55e3416b2e63cc56e46185b27a14799d48a2ac8d");
    background-repeat: no-repeat;
    background-size: stretch;
    background-position: left;
    background-color: black;
    border: none;
    }
    [data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
    }
    </style>
    """
        
    if "slider" not in st.session_state:
        st.session_state["slider"] = constants.NORMAL
    st.markdown(page_element, unsafe_allow_html=True)
   
    with header_left:
        st.markdown("<h1 style='color:red; font-family: Arial, sans-serif;'>Answer Grader</h1>", unsafe_allow_html=True)
    with _ :
        marking_style = st.select_slider('**Marking Style**', options=[constants.LENIENT, constants.NORMAL,  constants.STRICT], value=constants.NORMAL ,key= st.session_state["slider"])
    return marking_style

def footer():
    pass