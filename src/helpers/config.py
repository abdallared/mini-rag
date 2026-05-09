from pydantic_settings import BaseSettings , SettingsConfigDict 


class settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    FILE_ALLOWED_EXTENSIONS: list[str]
    FILE_MAX_SIZE: int
    DATA_DIR: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        
def get_settings(): 
    return settings()