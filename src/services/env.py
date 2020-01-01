from dotenv import load_dotenv
from os import getenv as environment_env

load_dotenv()

class Env():
    @staticmethod
    def api_client_secret_file():
        return environment_env("API_CLIENT_SECRET_FILE")

    @staticmethod
    def api_scope():
        return [environment_env("API_SCOPE", "https://www.googleapis.com/auth/youtube.force-ssl")]

    @staticmethod
    def api_service_name():
        return environment_env("API_SERVICE_NAME", "youtube")
    
    @staticmethod
    def api_version():
        return environment_env("API_VERSION", "v3")
    
    @staticmethod
    def api_token_storage():
        return environment_env("API_TOKEN_STORAGE")

    @staticmethod
    def comment_message():
        return environment_env("COMMENT_MSG", "First!")