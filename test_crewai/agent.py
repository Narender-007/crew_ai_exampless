from crewai import Crew,Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


researcher = Agent(
    role="crime batch police officer",
    goal="police officer under conver operation find drugs smuglers",
    verbose=True,
    memory=True,
    backstory="crime batch police officer have good exeperience previously, have solved many crime thriller cases "
    "he was found drugs dealers in hyderabad ,many celebraties interlinks with drug dealers"
    'police officer catched who are took and sold drugs.',
    tools = [search_tool],
    allow_delegation=True
)

writer = Agent(
    role="drug dealers",
    goal="drug dealers  drugs are sold in india main cities",
    verbose=True,
    memory=True,
    backstory="drug dealers are sold many areas in india they selling rich kids and celebraties"
    "police officers are not found drug dealers, because drug dealers are sleeper sells",
    tools = [search_tool],
    allow_delegation=True
)

