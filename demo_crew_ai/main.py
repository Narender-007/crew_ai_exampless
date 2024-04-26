import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

os.environ["OPENAI_API_KEY"] = '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'

# os.environ["OPENAI_ORGANIZATION"] = 'org-fgngWdr8MwLgakPMNAH6DFm5'
# os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.agent_1()
        custom_agent_2 = agents.agent_2()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.task_1(
            custom_agent_1,
            self.var1,
            self.var2,
        )

        custom_task_2 = tasks.task_2(
            custom_agent_2,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
            
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""enter name of the from location: """))
    var2 = input(dedent("""enter name of the to location: """))

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is Crew Ai result:")
    print("########################\n")
    print(result)