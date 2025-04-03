# MMM: Meeting Minutes Master

MMM (Meeting Minutes Master) is an AI-powered tool built with CrewAI and Streamlit that processes meeting transcripts, extracts key points, and generates structured notes and action items.

## Features
- 📝 Upload or paste a meeting transcript and get AI-generated structured minutes
- 🔊 Supports automatic audio transcription using Whisper
- ✅ Extracts action items automatically
- 📊 Displays CrewAI execution details, including token usage
- 🚀 Simple and intuitive Streamlit-based UI
- 🧹 Clear output with a single click

## Demo
[demo.webm](https://github.com/user-attachments/assets/1261943c-5713-4bd6-8750-284004db6705)

## Understanding MMM Crew

The MeetingMinutesMaster Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## Technologies Used
- **Python** – Core programming language
- **Streamlit** – For interactive UI
- **CrewAI** – AI-powered meeting processing
-  **Whisper** – For automatic speech-to-text transcription

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system.

1.  **Create a Virtual Environment:**
    It's recommended to create a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install Dependencies:**
    Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
    *Note:* This project uses [UV](https://docs.astral.sh/uv/) for potentially faster dependency management. If you have `uv` installed (`pip install uv`), you can often use `uv pip install -r requirements.txt` for quicker installation.

3.  **Add API Key:**
    Copy the `.env.example` file to `.env` and add your `GROQ_API_KEY`:
    ```bash
    cp .env.example .env
    # Now edit the .env file and add your key
    ```

## Running the Project

To run the Meeting Minutes Master application:

```bash
streamlit run src/meetingminutes/main.py
```

> **Important Notes:**
> *   **First Run:** The first time you run the application, it will download the Whisper model for audio transcription. This might take some time depending on your internet speed and the model size chosen.
> *   **Whisper Model Size:** If you experience performance issues or have limited hardware resources, consider using smaller Whisper models (e.g., 'tiny', 'base'). You might need to adjust the model selection within the application code (`src/meetingminutes/transcription.py` or similar) if this option isn't exposed in the UI.

## Roadmap

Here's a glimpse into the future plans for MMM:

- [ ] **Ollama Support:** Integrate local LLM support via Ollama for enhanced privacy and offline capabilities.
- [ ] **UI Revamp:** Rebuild the user interface using React for a more modern and potentially more interactive experience.
- [ ] **Docker Support:** Provide Dockerfile and docker-compose configurations for easier deployment and environment consistency.

## Contributing
Feel free to fork the repository and submit pull requests! Contributions are always welcome.


## Author
Created by [Abu Bakar Siddik] - [[GitHub Profile](https://github.com/Bakar31)]
