import os
os.environ["OPENAI_API_KY"] = ''


from crewai import Crew, Process, Agent, Task



# Define your agents

researcher = Agent(

  role='Researcher',

  goal='Conduct foundational research',

  backstory='An experienced researcher with a passion for uncovering insights'

)

analyst = Agent(

  role='Data Analyst',

  goal='Analyze research findings',

  backstory='A meticulous analyst with a knack for uncovering patterns'

)

writer = Agent(

  role='Writer',

  goal='Draft the final report',

  backstory='A skilled writer with a talent for crafting compelling narratives'

)



# Define the tasks in sequence

research_task = Task(description='Gather relevant data...', agent=researcher,expected_output="based on tasks")

analysis_task = Task(description='Analyze the data...', agent=analyst,expected_output="based on tasks")

writing_task = Task(description='Compose the report...', agent=writer,expected_output="based on tasks")



# Form the crew with a sequential process

report_crew = Crew(

  agents=[researcher, analyst, writer],

  tasks=[research_task, analysis_task, writing_task],

  process=Process.sequential

)

result = report_crew.kickoff()
print(result)