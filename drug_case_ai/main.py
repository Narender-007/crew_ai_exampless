import os
os.environ["OPENAI_API_KEY"] = ''

from crewai import Crew, Process, Agent, Task
from agent import researcher, analyst, writer

# Define your agents
city = input("enter the name of city:")
month = input("enter the name of month:")



# Form the crew with a sequential process

report_crew = Crew(

  agents=[researcher, analyst, writer],

  tasks=[research_task, analysis_task, writing_task],

  process=Process.sequential

)

result = report_crew.kickoff()
print(result)