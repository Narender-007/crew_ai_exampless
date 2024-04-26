from crewai import Task
from crewai_tools import SerperDevTool
from agent import writer,researcher
search_tool = SerperDevTool()



# Define the tasks in sequence

research_task = Task(description='gather the theaters and released movies on the week, find the best comedy and entainment movies on the {month}, theaters should be get from particular location {city}. the best and clean theatres need to be result and find the all type of theatres like single scrreen ,multiplex,malls theatres', agent=researcher,expected_output="your final answer is month of all releas movies ")

analysis_task = Task(description='anaylyze the best movies in the city {city}, and comfort and does not any distubance from theatre side and well and good analyze the theatres. ', agent=analyst,expected_output="your final answer is best movies in theatres")

writing_task = Task(description='you writtent well and good find theatres in the input {city} city location ', agent=writer,expected_output="your final answer is best movies in theatres")



