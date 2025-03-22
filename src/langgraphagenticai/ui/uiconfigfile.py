from configparser import ConfigParser

class Config:
    def __init__(self,config_file="D:\AgenticAI\LangGraphProject\src\langgraphagenticai\ui\uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
        

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")      
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_grq_model_option(self):
        return self.config["DEFAULT"].get
        
        
        