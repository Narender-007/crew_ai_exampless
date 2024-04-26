from crewai import Task
from crewai_tools import SerperDevTool
from agent import writer,researcher
search_tool = SerperDevTool()


# Research task

# research_task = Task(

#   description=(

#     "Identify the most drug dealer in {topic}."

#     "Focus on identifying pros and cons and the overall narrative."

#     "Your final report should clearly articulate the key points,"


#   ),

#   expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',

#   tools=[search_tool],

#   agent=researcher,

# )



# # Writing task with language model configuration

# write_task = Task(

#   description=(

#     "Compose an insightful article on {topic}."

#     "Focus on the latest trends and how it's impacting the industry."

#     "This article should be easy to understand, engaging, and positive."

#   ),

#   expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',

#   tools=[search_tool],

#   agent=writer,

#   async_execution=False,

#   output_file='new-blog-post.md'  # Example of output customization

# )



# Research task

research_task = Task(

  description=(

    "Identify the most drug dealer in {topic}."

    "Focus on identifying pros and cons and the overall narrative."

    "Your final report should clearly articulate the key points,"


  ),

  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',

  tools=[search_tool],

  agent=researcher,

)



# Writing task with language model configuration

write_task = Task(

  description=(

    "Compose an insightful article on {topic}."

    "Focus on the latest trends and how it's impacting the industry."

    "This article should be easy to understand, engaging, and positive."

  ),

  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',

  tools=[search_tool],

  agent=writer,

  async_execution=False,

  output_file='new-blog-post.md'  # Example of output customization

)