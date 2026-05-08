from pydantic_settings import BaseSettings , settings_configDict


class settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str

    class Config:
        env_file = "/src/.env"
        env_file_encoding = "utf-8"
        
        
def get_settings(): 
    return settings()