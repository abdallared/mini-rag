from controllers.BaseController import BaseController
from helpers.config import settings
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        
    def validate_file(self , file: UploadFile):
        
        # Validate file extension
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False
        
        # Validate file size
        if file.size > self.app_settings.FILE_MAX_SIZE:
            return False
        
        return True 