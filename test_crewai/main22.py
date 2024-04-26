import os
os.environ["OPENAI_API_KEY"] = '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'

from crewai import Crew, Process, Agent, Task

# Define your agents
city = input("enter the name of city:")
bank = input("enter the name of bank:")
researcher = Agent(

  role='city selection expert',

  goal='Select the best branch based on good communication and only city locations.',

  backstory='Expert at analyzing all bank brnaches data to pick ideal destinations'

)

analyst = Agent(

  role='branch locations expert',

  goal='provide the all branches name and locations.',

  backstory='An exeperienced have best knowledge about bank and branches names. '

)

# writer = Agent(

#   role='Expert in select best movies',

#   goal='select best movies in the city with good seating and rating reviews about the theater and movies ',

#   backstory='an exeperienced finding the best movies in theatres'

# )

# Define the tasks in sequence

research_task = Task(description = "find the bank of all branch locations for the account opening, good features ,good communication with customers.                  **Parameters**: - city: {city} - bank: {bank} ", agent=researcher,expected_output="your final answer is the report all bank of branch locations.")

analysis_task = Task(description ='find the list of bank branch locaitons in the city     **Parameters**: - city: {city} - bank: {bank} ', agent=analyst,expected_output="your final answer is report the all bank of branch locations.")

# writing_task = Task(description ='collect the list of recent released movies name with theater name and show timings and how much price of the cost each class seating.', agent=writer,expected_output="your final answer is best movies in theatres")

# Form the crew with a sequential process

report_crew = Crew(

  agents=[researcher, analyst],#, writer],

  tasks=[research_task, analysis_task],

  process=Process.sequential

)

result = report_crew.kickoff()
print(result)