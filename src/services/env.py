from dotenv import load_dotenv
from os import getenv as environment_env

load_dotenv()

class Env():
    @staticmethod
    def clock_time_zone():
        valid_time_zones = ["est", "utm", "gtm"]
        time_zone = environment_env("CLOCK_TIME_ZONE")

        if time_zone not in valid_time_zones:
            return valid_time_zones[0]
        
        return time_zone

    @staticmethod
    def clock_api_url():
        return "http://worldclockapi.com/api/json/{time_zone}/now".format(
            time_zone=Env.clock_time_zone()
        )

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