from dotenv import load_dotenv
from os import getenv as environment_env

load_dotenv()

class Env():
    @staticmethod
    def comment_message():
        return environment_env("COMMENT_MSG", "First!")