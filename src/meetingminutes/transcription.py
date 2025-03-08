import streamlit as st
import whisper
import tempfile
import logging
from utils import handle_error


def process_uploaded_audio(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
            temp_audio.write(uploaded_file.read())
            audio_file_path = temp_audio.name

        transcribe_audio(audio_file_path)
    except Exception as e:
        handle_error("Error processing uploaded audio", e)


def transcribe_audio(audio_file_path):
    try:
        st.info("⏳ Transcribing audio...")
        st.session_state.transcription_status = "Transcribing..."

        model = whisper.load_model(st.session_state.whisper_model_name)
        result = model.transcribe(audio_file_path)

        st.session_state.meeting_transcript = st.text_area(
            "✍️ Meeting Transcript:", value=result["text"], height=300
        )
        st.session_state.transcription_status = "Transcription Complete."
        st.success(st.session_state.transcription_status)
        logging.info("Audio transcription successful.")
    except Exception as e:
        handle_error("Error during transcription", e)
