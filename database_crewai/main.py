from crewai_tools import PGSearchTool
import os
os.environ["OPENAI_API_KEY"] = ''



# Initialize the tool with the database URI and the target table name

# tool = PGSearchTool(db_uri='postgresql://postgres:123456@localhost:5433/vk_local_dbb', table_name='customer_vk_customer')
tool = PGSearchTool(
    db_uri='postgresql://postgres:123456@localhost:5433/vk_local_dbb', table_name='customer_vk_customer',

    config=dict(

        llm=dict(

            provider="ollama", # or google, openai, anthropic, llama2, ...

            config=dict(

                model="llama2",

                # temperature=0.5,

                # top_p=1,

                # stream=true,

            ),

        ),

        embedder=dict(

            provider="google",

            config=dict(

                model="models/embedding-001",

                task_type="retrieval_document",

                # title="Embeddings",

            ),

        ),

    )

)

print(tool.run)