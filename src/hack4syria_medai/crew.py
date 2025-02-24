from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class Hack4SyriaMedai:
    """Hack4SyriaMedai crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Instantiate tools
    search_tool = SerperDevTool()

    @agent
    def translation_agent(self) -> Agent:
        print(f"Translation agent config: {self.agents_config['translation_agent']}")
        return Agent(config=self.agents_config["translation_agent"], verbose=True)

    @agent
    def privacy_agent(self) -> Agent:
        return Agent(config=self.agents_config["privacy_agent"], verbose=True)

    @agent
    def first_line_support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["first_line_support_agent"], verbose=True
        )

    @agent
    def diagnosis_agent(self) -> Agent:
        return Agent(config=self.agents_config["diagnosis_agent"], verbose=True)

    @agent
    def cardiology_specialist_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["cardiology_specialist_agent"], verbose=True
        )

    @agent
    def medical_knowledge_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["medical_knowledge_agent"],
            verbose=True,
            tools=[self.search_tool],
        )

    @agent
    def final_output_agent(self) -> Agent:
        return Agent(config=self.agents_config["final_output_agent"], verbose=True)

    @task
    def translation_to_ar(self) -> Task:
        print(f"{self.tasks_config['translation_to_ar']}")
        return Task(
            config=self.tasks_config["translation_to_ar"],
            agent=self.translation_agent(),
            output_file="output/1.translated_text_ar.md",
        )

    @task
    def privacy_check(self) -> Task:
        return Task(
            config=self.tasks_config["privacy_check"],
            agent=self.privacy_agent(),
            output_file="output/2.privacy_check_output.md",
        )

    @task
    def information_gathering(self) -> Task:
        return Task(
            config=self.tasks_config["information_gathering"],
            agent=self.first_line_support_agent(),
            output_file="output/3.information_gathering_output.md",
        )

    @task
    def initial_diagnosis(self) -> Task:
        return Task(
            config=self.tasks_config["initial_diagnosis"],
            agent=self.diagnosis_agent(),
            output_file="output/4.initial_diagnosis_output.md",
        )

    @task
    def cardiac_consultation(self) -> Task:
        return Task(
            config=self.tasks_config["cardiac_consultation"],
            agent=self.cardiology_specialist_agent(),
            output_file="output/5.cardiac_consultation_output.md",
        )

    @task
    def medical_validation(self) -> Task:
        return Task(
            config=self.tasks_config["medical_validation"],
            agent=self.medical_knowledge_agent(),
            output_file="output/6.medical_validation_output.md",
        )

    @task
    def final_report_generation(self) -> Task:
        return Task(
            config=self.tasks_config["final_report_generation"],
            agent=self.final_output_agent(),
            output_file="output/7.final_report_en.md",
        )

    @task
    def final_translation(self) -> Task:
        return Task(
            config=self.tasks_config["final_translation"],
            agent=self.translation_agent(),
            output_file="output/8.final_report_ar.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Hack4SyriaMedai crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
