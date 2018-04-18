import yaml 
import logging.config
import os

__author__='bill'

class Logger:
    
    def setup_logging(self,default_path="lib\logging.yaml",default_level=logging.INFO,env_key="LOG_CFG"):
        path=default_path
        value=os.getenv(env_key,None)
        if value:
            path=value
        if os.path.exists(path):
            with open(path, "r") as f:
                config=yaml.load(f)
                print(f"------{config}------")
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
    


