import logging
import streamlit as st
from ui import setup_ui, handle_buttons
from state import initialize_state
from transcription import process_uploaded_audio


def main():
    setup_ui()
    initialize_state()
    handle_user_input()


def handle_user_input():
    uploaded_file = st.file_uploader(
        "Upload Meeting Recording", type=["mp3", "mp4", "wav", "webm"]
    )

    if uploaded_file:
        process_uploaded_audio(uploaded_file)
    else:
        st.session_state.meeting_transcript = st.text_area(
            "✍️ Paste Meeting Transcript Here:", height=300
        )

    handle_buttons()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
