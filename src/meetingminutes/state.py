import streamlit as st


def initialize_state():
    for key in [
        "transcription_status",
        "processing_status",
        "output_status",
        "meeting_transcript",
    ]:
        if key not in st.session_state:
            st.session_state[key] = None
