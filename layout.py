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
                
                # try:
                score = grader(uploaded_files, uploaded_text, rubric, marking_style)
                # except:
                #     st.error("Error while grading")
                    

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

    background-image: url("https://mcdn.wallpapersafari.com/medium/0/8/UItQvK.jpg");
 
    background-size: cover;
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
        st.title("Answer Grader")
    with _ :
        marking_style = st.select_slider('**Marking Style**', options=[constants.NORMAL, constants.LENIENT, constants.STRICT], key= st.session_state["slider"])
    return marking_style

def footer():
    pass