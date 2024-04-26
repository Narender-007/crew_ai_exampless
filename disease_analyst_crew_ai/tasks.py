from crewai import Task
from agents import researcher,writer,analyst 
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

research_task = Task(
    description="Research the new diseases in India. People are experiencing symptoms such as sneezing, fever, and coughing, while some are also reporting body pains. They are not feeling well, with red eyes and symptoms indicative of viral fever.",
    agent=researcher,
    expected_output="you will find what is the disease based on that symptoms.",
    Tools=[search_tool]
    )


analyse_task = Task(
    description="Analyze the diseases prevalent in India, their effects on the human body, and the necessary precautions that are important.",
    agent=analyst,
    expected_output="you will give the precautions based on disease.",
    Tools=[search_tool]
)

writer_task = Task(
    description="Prepare the document outlining various diseases and their implications for health. Include details on the precautions necessary to maintain a healthy body.",
    agent=writer,
    expected_output="",
    Tools=""
)

