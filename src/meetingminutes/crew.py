from datetime import datetime
import os
from crewai import Agent, Crew, Flow, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Meetingminutes():
    """Meeting minutes processing crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def transcriber(self) -> Agent:
        return Agent(
            config=self.agents_config['transcriber'],
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )

    @agent
    def action_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['action_extractor'],
            verbose=True
        )

    @task
    def transcribe_task(self) -> Task:
        return Task(
            config=self.tasks_config['transcribe_task']
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task']
        )

    @task
    def action_task(self) -> Task:
        meeting_notes_dir = "meeting_notes"
        os.makedirs(meeting_notes_dir, exist_ok=True) 
            
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        output_file= f"{meeting_notes_dir}/{timestamp}_action_items.md"
        return Task(
            config=self.tasks_config['action_task'],
            
            output_file=output_file
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Meetingminutes crew"""

        return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)
