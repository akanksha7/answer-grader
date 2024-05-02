import streamlit as st
from streamlit.logger import get_logger
from layout import body


LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Answer Grader",
        layout='wide'
        
    )

    body()

if __name__ == "__main__":
    run()
