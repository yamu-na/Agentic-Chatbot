from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represt the structure of the state used in the graph
    
    """
    messages: Annotated[List, add_messages]
    news_data: list
    summary: str
    filename: str

   