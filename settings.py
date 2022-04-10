from distutils.command.upload import upload
from pydantic import BaseConfig

class Config(BaseConfig):
    aws_access_key: str = 'your_access_key'
    aws_secret_access_key: str = 'your_secert_access_key'
    upload_file__bucket: str = 'your_upload_file__bucket'
    upload_folder: str = 'dummy/'
