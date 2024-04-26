from crewai import Crew,Process,Agent
from crewai import Agent
import os

os.environ["SERPER_API_KEY"] = "bcaaa25c1c4ccfbf6fc8c3ffc189d4fb78c48f28"  # serper.dev API key

os.environ["OPENAI_API_KEY"] = "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"


researcher = Agent(role="Researcher New Disease",
                   goal="uncover groundbreaking the news about {}",
                   backstory="expert in the found new disease news"
                   "you have great knowledge about new things researching"
                   )


analyst = Agent(role="analysist",
                goal="analyze the topic based on the research analysis",
                backstory="expert in the topic analysist"
                "whcih type of disease in india most popular")


writer = Agent(role="writer",
               goal=" prepare two A4 documents of data need to collect",
               
               backstory="expert in the prepare A4 sheet document about new disease"
               " find and research write th document ")

