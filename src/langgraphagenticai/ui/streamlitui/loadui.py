import streamlit as st 
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control={}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title="Agentic AI" + self.config.get_page_title(), layout="wide")
        st.header("Agentic" + self.config.get_page_title())
        st.session_state.timeframe=""
        st.session_state.IsFecthButtonClicked = False
        st.session_state.IsSDLC = False
        
        
        with st.sidebar:
            #Get Option from config
            llm_option = self.config.get_llm_option()
        
        
        
    
        