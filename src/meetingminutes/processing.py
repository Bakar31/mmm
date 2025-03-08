import streamlit as st
import logging
from datetime import datetime
from crew import Meetingminutes
from utils import handle_error


def process_meeting(meeting_transcript):
    if not meeting_transcript or not meeting_transcript.strip():
        st.warning("⚠️ Please paste or upload a meeting transcript before processing.")
        return

    st.session_state.processing_status = "Processing..."
    st.info("⏳ Processing your meeting transcript...")

    try:
        inputs = {
            "meeting_transcript": meeting_transcript,
            "current_year": str(datetime.now().year),
        }
        crew_output = Meetingminutes().crew().kickoff(inputs=inputs)
        display_results(crew_output)
        st.session_state.processing_status = "Processing Complete."
        st.success(st.session_state.processing_status)
        logging.info("Meeting processing successful.")
    except Exception as e:
        handle_error("Error during meeting processing", e)


def display_results(crew_output):
    st.subheader("✅ Action Items")
    st.markdown(f"```\n{crew_output.raw}\n```")

    st.subheader("📊 Crew Execution Details")
    token_details = f"""
    - **Total Tokens:** {crew_output.token_usage.total_tokens}
    - **Prompt Tokens:** {crew_output.token_usage.prompt_tokens}
    - **Cached Prompt Tokens:** {crew_output.token_usage.cached_prompt_tokens}
    - **Completion Tokens:** {crew_output.token_usage.completion_tokens}
    - **Successful Requests:** {crew_output.token_usage.successful_requests}
    """
    st.markdown(token_details)

    if isinstance(crew_output.json_dict, dict):
        st.subheader("📜 Structured Output")
        st.json(crew_output.json_dict)

    st.session_state.output_status = "Output Generated."
    st.success(st.session_state.output_status)
