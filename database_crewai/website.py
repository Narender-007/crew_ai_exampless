from crewai_tools import WebsiteSearchTool

import os
os.environ["OPENAI_API_KEY"] = ''


# Example of initiating tool that agents can use to search across any discovered websites

tool = WebsiteSearchTool()



# Example of limiting the search to the content of a specific website, so now agents can only search within that website

tool = WebsiteSearchTool(website='https://docs.crewai.com/tools/WebsiteSearchTool/#installation')
print(tool.run)