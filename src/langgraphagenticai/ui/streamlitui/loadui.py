import streamlit as st 
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}
        
        
    def initialize_session(self):
        return{
            "current_step": "requirements",
            "requirememnts":"",
            "user_stories":"",
            "po_feedback": "",
            "generated_code":"",
            "rerview_feedback":"",
            "decision":None 
        }
        
    
    def render_requirements(self):
        st.markdown("## Requirements Submission ")
        st.session_state["requirements"] = st.text_area(
            "Enter your requirements:",
            height=200,
            key="req_input"
        )
    
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title="Agentic AI" + self.config.get_page_title(), layout="wide")
        st.header("Agentic" + self.config.get_page_title())
        st.session_state.timeframe=""
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        
        with st.sidebar:
            #Get Option from config
            llm_option = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_options()
            
            #LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_option)
            
            if self.user_controls["selected_llm"] == 'Groq':
                # Model Selection
                model_options = self.config.get_groq_model_option()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                #API KEY input and Validation
                self.user_controls["GROQ_API_KEY"] = st.session_state["groq_API_KEY"] = st.text_input("API Key", type="password")
                
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please Enter your Groq API Key to proceed. Don't heve refer : https://console.groq.com/keys " )
                    
        ##UseCase Selection           
                    
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecase",usecase_options)
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            
            
        return self.user_controls
            
            
        
        
    
        