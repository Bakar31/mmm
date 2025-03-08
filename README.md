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

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/meetingminutes/config/agents.yaml` to define your agents
- Modify `src/meetingminutes/config/tasks.yaml` to define your tasks
- Modify `src/meetingminutes/crew.py` to add your own logic, tools and specific args
- Modify `src/meetingminutes/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the MeetingMinutes Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Contributing
Feel free to fork the repository and submit pull requests! Contributions are always welcome.


## Author
Created by [Abu Bakar Siddik] - [[GitHub Profile](https://github.com/Bakar31)]
