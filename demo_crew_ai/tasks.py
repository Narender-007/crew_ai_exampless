from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            
            {self.__tip_section()}
    
            anaylze and select best average fare charges online tickets,
            ticket discounts ,and seat availability.
            
    
            Use this variable: {var1}
            And also this variable: {var2}
        """
            ),
            agent=agent,
            expected_output='A refined finalized version of the blog post in markdown format'

        )

    def task_2(self, agent):
        return Task(
            description=dedent(
                f"""
                                       
            {self.__tip_section()}

            anaylze and select best average fare charges online tickets,
            ticket discounts and seat availability.
        """
            ),
            agent=agent,
            expected_output='A refined finalized version of the blog post in markdown format'

        )
