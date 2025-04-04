from typing import Annotated, Literal, Optional, TypedDict, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    """
    Represents The structure of the state used in the graph
    """
    
    messages: Annotated[list, add_messages]
    