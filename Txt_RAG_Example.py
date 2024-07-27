import os
from langchain_community.llms import Ollama
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools.tools import TXTSearchTool

rag_tool = TXTSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama3",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            )
        ),
        embedder=dict(
            provider="ollama", # or openai, ollama, ...
            config=dict(
                model="mxbai-embed-large",
                # task_type="retrieval_document",
                # title="Embeddings",
            )
        ),
        chunker=dict(
            chunk_size=400,
            chunk_overlap=20,
            min_chunk_size=100
        )
    ),
    #txt='/Users/aakashsuresh/Desktop/VSProject/Crew_AI_Examples/Text_RAG_Example/sample_data/test.txt'
    txt = 'sample_data/test.txt'
)


llm1 = Ollama(
    temperature=0,
    model = "llama3",
    base_url = "http://localhost:11434")

def main():
    data_analyst = Agent(
    role='Expert Story interpreter',
    goal='Answer the question by understanding the story given',
    backstory='you are an expert user of rag_tool to read the text file , and handle the task given',
    verbose=True,
    allow_delegation=False,
    llm=llm1,
    tools=[rag_tool]
    )

    test_task = Task(
    description="Make a list of all characters in the story ",
    expected_output= "one line information",
    agent=data_analyst
    )

    result = test_task.execute()
    print(result)

if __name__ == "__main__":
    main()