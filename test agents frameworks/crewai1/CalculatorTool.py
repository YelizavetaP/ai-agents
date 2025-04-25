from langchain_community.tools import tool


# define a tool
@tool("Calculate")
def calculate_tool(equation: str):
    # for agent to understand the tool
    """Use this to calculate the result of a math equation"""

    return eval(equation)




