import os
from crewai import Agent, Task, Crew
# to use .env file
from dotenv import load_dotenv

# load the variables in .env file
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")


info_agent = Agent(
    role="Information Agent",
    goal="Give information about certain topic",
    backstory="""You are a helpful assistant 
                that loves to know information
                and share it with others"""
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
    # verbose=2
)



result = crew.kickoff()

print(result)