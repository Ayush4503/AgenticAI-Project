import streamlit as st 
import json

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langraph_agenticai_app():
    """Load and run the LnagGraph AgenticAI application with streamlit ui>"""
    
    #Loa UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Text input for user message 
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
        
    else:
        user_message = st.chat_input("Enter your message: ")
        
    if user_message:
            try:
                
                obj_llm_config = GroqLLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()

                if not model:
                    st.error("Error: LLM model could not be initialized.")
                    return
                
                #initialize and set up the graph based on use case
                
                usecase = user_input.get('selected_usecase')
                if not usecase:
                    st.error("Error: No use case selected")
                    return
                
                ##Graph Builder
                
                graph_builder = GraphBuilder(model)
                try:
                    graph = graph_builder.setup_graph(usecase)
                    DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
                
                except Exception as e:
                    st.error(f"Error: Graph setup Failed = {e}")
                    return
            
            
            except Exception as e:
                raise ValueError(f"Error Occured with Exception:{e}")