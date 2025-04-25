import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from langchain_community.llms import Ollama

# load the variables in .env file
load_dotenv()

# Initialize Ollama
llm = Ollama(
    model="Phi-3",
    base_url="http://localhost:11434"
)

info_agent = Agent(
    role="Information Agent",
    goal="Give information about certain topic",
    backstory="""You are a helpful assistant 
                that loves to know information
                and share it with others""",
    llm=llm,
    verbose=True
)

task1= Task(
    # what need to be done
    description="Tell me all u know about lemon shark",
    # what expected output
    expected_output="A quick summary and then 7 bullet points about the topic",
    # what agent to use
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print(result)