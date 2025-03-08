import streamlit as st


def setup_ui():
    st.set_page_config(
        page_title="Meeting Minutes Master", page_icon="📝", layout="centered"
    )
    st.title("📝 Meeting Minutes Master (MMM)")
    st.markdown(
        "MMM processes meeting transcripts, extracts key points, and generates structured notes."
    )

    setup_sidebar()


def setup_sidebar():
    st.sidebar.header("⚙️ MMM Settings")
    st.session_state.whisper_model_name = st.sidebar.selectbox(
        "Select Whisper Model", ["tiny", "base", "small", "medium", "large"], index=2
    )


def handle_buttons():
    col1, col2 = st.columns(2)

    with col1:
        process_button = st.button("🚀 Process Meeting")
    with col2:
        clear_button = st.button("🧹 Clear Output")

    if clear_button:
        reset_state()

    if process_button:
        from processing import process_meeting

        process_meeting(st.session_state.meeting_transcript)


def reset_state():
    for key in [
        "transcription_status",
        "processing_status",
        "output_status",
        "meeting_transcript",
    ]:
        st.session_state[key] = None
    st.rerun()
