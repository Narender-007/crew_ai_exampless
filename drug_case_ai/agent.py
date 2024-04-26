from crewai import Crew,Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


researcher = Agent(

  role='Researcher',

  goal='Conduct foundational research',

  backstory='An experienced researcher finding the new release movies in month'

)

analyst = Agent(

  role='Data Analyst',

  goal='Analyze research findings',

  backstory='you had expert finding best movie release dates particulart location, movie details ,in side '

)

writer = Agent(

  role='finder',

  goal='analyze the best movies and theaters in the city',

  backstory='you had expert in the entertainment movies released on the current month and movies name and release date and ticket price also.'

)
