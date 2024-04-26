from crewai import Crew,Process
from crewai_tools import SerperDevTool
from agents import researcher,writer,analyst
from tasks import research_task,analyse_task,writer_task
import os
os.environ["SERPER_API_KEY"] = "bcaaa25c1c4ccfbf6fc8c3ffc189d4fb78c48f28"  # serper.dev API key

os.environ["OPENAI_API_KEY"] = ""



search_tool = SerperDevTool()


disease_crew = Crew(agents=[researcher,analyst,writer],
                    tasks=[research_task,analyse_task,writer_task])

result_data = disease_crew.kickoff()
print(result_data)

