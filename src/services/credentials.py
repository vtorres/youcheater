import pickle

from googleapiclient.discovery import build as oauth_builder
from google_auth_oauthlib.flow import InstalledAppFlow as oauth_flow
from google.auth.transport.requests import Request as oauth_request
from os import path as environment_path

from .env import Env

class Credentials:
    API_SCOPE = Env.api_scope()
    API_SECRET_FILE = Env.api_client_secret_file()
    API_SERVICE_NAME = Env.api_service_name()
    API_TOKEN_STORAGE_PATH = Env.api_token_storage()
    API_VERSION = Env.api_version()

    @staticmethod
    def build():
        creds = None
        if environment_path.exists(Credentials.API_TOKEN_STORAGE_PATH):
            with open(Credentials.API_TOKEN_STORAGE_PATH, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(oauth_request())
            else:
                flow = oauth_flow.from_client_secrets_file(
                    Credentials.API_SECRET_FILE,
                    Credentials.API_SCOPE
                )
                creds = flow.run_console()
            with open(Credentials.API_TOKEN_STORAGE_PATH, 'wb') as token:
                pickle.dump(creds, token)

        return oauth_builder(Credentials.API_SERVICE_NAME, Credentials.API_VERSION, credentials=creds)
