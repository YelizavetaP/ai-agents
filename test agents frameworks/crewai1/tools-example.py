import os
from crewai import Agent, Task, Crew, Process
# to use .env file
from dotenv import load_dotenv
from CalculatorTool import calculate_tool

# load the variables in .env file
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")


print('## Welcome to the CrewAI Math Example')
math_input = input('Enter a math equation: ')


math_agent = Agent(
    role='Math Expert',
    goal='Solve the math equation',
    backstory='You are a math expert with a passion for solving complex equations',
    verbose=True,
    tools=[calculate_tool],
)



writer_agent = Agent(
    role='Writer',
    goal='Write a compelling explanation of the results of the math equation',
    backstory="""You are a writer with a passion 
    for writing engaging articles with explanations 
    of complex things in a simple way""",
    verbose=True,
)



task1 = Task(
    # what need to be done
    description = math_input,
    # how format the output
    expected_output="Give full details in bullet points",
    # what agent to use
    agent=math_agent
)

task2 = Task(
    description = """Use the results provided write a detailed explanation how it works""",
    # how format the output
    expected_output="""Explain in full details and save in markdown format.
    Do not add triple backticks in the output.
    Also dont say what type it is in the first line""",
    # where to save the output
    # output_file="math.md",
    # create_directory=True,
    # what agent to use
    agent=writer_agent
)


crew = Crew(
    agents=[math_agent, writer_agent],
    tasks=[task1, task2],
    # how to process the tasks
    process=Process.sequential,
    verbose=2
)


result = crew.kickoff()
print(result)




















