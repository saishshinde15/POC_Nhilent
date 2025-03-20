from decimal import Context
from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

# Initialize the tool
file_writer_tool = FileWriterTool()

llm = LLM(
    model="ollama/llama3.1:latest",
    base_url="http://localhost:11434"
)


@CrewBase
class Nihilentpoc():
	"""Nihilentpoc crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def code_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['code_writer'],
			verbose=True,
			llm=llm
		)

	@agent
	def code_executor(self) -> Agent:
		return Agent(
			config=self.agents_config['code_executor'],
			verbose=True,
			tools=[file_writer_tool],
			llm=llm,
			allow_code_execution=True,
		)


	@task
	def modify_file_task(self) -> Task:
		return Task(
			config=self.tasks_config['modify_file_task'],
			agent=self.code_writer
		)

	@task
	def execute_and_save_task(self) -> Task:
		return Task(
			config=self.tasks_config['execute_and_save_task'],
			context=[self.modify_file_task],
			agent=self.code_executor
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Nihilentpoc crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)