import streamlit as st
from streamlit.logger import get_logger
from layout import frontend


LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Answer Grader",
        layout='wide'
    )

    frontend()

if __name__ == "__main__":
    run()
