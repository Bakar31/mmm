import streamlit as st
import logging


def handle_error(message, exception):
    logging.error(f"{message}: {exception}")
    st.error(f"❌ {message}: {exception}")
    st.session_state.processing_status = "Failed."
    st.error(st.session_state.processing_status)
