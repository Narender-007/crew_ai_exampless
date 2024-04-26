from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def agent_1(self):
        return Agent(
            role="researcher ticket agent",
            backstory=dedent(f"""exepert in online tickets availability"""),
            goal=dedent(f"""find online bus tickets available."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
            tools=[
                SearchTools.search_internet,
            ],
        )

    def agent_2(self):
        return Agent(
            role="analysis agent",
            backstory=dedent(f"""you are exepert in ticket booking systems"""),
            goal=dedent(f"""find online ticket fare ,bookings availability"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
            tools=[
                SearchTools.search_internet,

            ],

        )
