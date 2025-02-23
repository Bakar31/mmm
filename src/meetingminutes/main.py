import sys
import warnings
import os
import streamlit as st
import json
from datetime import datetime
from crew import Meetingminutes
from dotenv import load_dotenv

load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

st.set_page_config(page_title="Meeting Minutes Processor", page_icon="📄", layout="centered")

st.title("📄 Meeting Minutes Analyzer")
st.markdown("Paste your meeting transcript below and generate structured notes & action items with AI-powered processing.")

meeting_transcript = st.text_area("✍️ Paste Meeting Transcript Here:", height=300)
col1, col2 = st.columns(2)

with col1:
    process_button = st.button("🚀 Process Meeting")
with col2:
    clear_button = st.button("🧹 Clear Output")

if clear_button:
    st.rerun()

if process_button:
    if not meeting_transcript.strip():
        st.warning("⚠️ Please paste a meeting transcript before processing.")
    else:
        process_button = st.button("⏳ Processing...", disabled=True)
        st.info("⏳ Processing your meeting transcript...")

        try:
            inputs = {"meeting_transcript": meeting_transcript, "current_year": str(datetime.now().year)}
            crew_output = Meetingminutes().crew().kickoff(inputs=inputs)
            results = {}
            if isinstance(crew_output.tasks_output, list):
                for task in crew_output.tasks_output:
                    if isinstance(task, dict): 
                        results.update(task)

            st.subheader("✅ Action Items")
            st.markdown(f"""
            ```
            {crew_output.raw}
            ```
            """)

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
        
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")