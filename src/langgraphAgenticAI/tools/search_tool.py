import os
from langchain_tavily import TavilySearch 
from langgraph.prebuilt import ToolNode


def get_tools(tavily_api_key):
    """
    Return the list of tools to be used in the chatbot.
    """
    # print("Creating Tavily tool...")

    os.environ["TAVILY_API_KEY"] = tavily_api_key

    tools = [
        TavilySearch(max_results=2)
    ]

    return tools


def create_tool_node(tools):
    """
    Creates and returns a ToolNode.
    """
    return ToolNode(tools)