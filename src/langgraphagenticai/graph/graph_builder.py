from langgraph.graph import StateGraph, END, MessagesState, START
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_cahtbot_node import BasicChatbotNode



class GraphBuilder:
    def __init__(self, model):
        self.llm=model
        self.graph_builder=StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        """Build a Basic chatbot using langgraph.
        This method initializes a chatbot node using the 'BasiChatBotNode'
        class and itegrated it into the graph."""
        
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot",END)
        
        
        
        
    
        
        
        