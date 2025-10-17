from pydantic_settings import BaseSettings

class settings(BaseSettings):

    database_username : str
    database_password : str
    database_hostname : str
    database_port : str
    database_name : str
    database_url : str
    
    class Config:
        env_file = ".env"

setting = settings()
        
