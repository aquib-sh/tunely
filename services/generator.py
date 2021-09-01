import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

 
class TokenGenerator:
    
    def generate_google_api_token(self, client_secret: str, scopes: list):
        """Generates a Google API Token from scratch, user login and auth would be required.
        
        Parameters
        ----------
        client_secret: str
            Path to the client secret json file.

        scopes: list
            Scopes of the token.
        """
        # Get token from the user
        flow = InstalledAppFlow.from_client_secrets_file(client_secret, scopes)
        creds = flow.run_console()
        return creds


    def export_token(self, token, output_path: str):
        """Outputs the token as JSON file.
        
        Parameters
        ----------
        token
            Token to output.

        output_path: str
            Path to where token will be exported.
        """
        with open(output_path, "w") as fp:
            fp.write(token.to_json())


    def retrieve_google_api_token(self, token_path: str, scopes: list):
        """Retrieves the token from a file.
        
        Parameters
        ----------
        token_path: str
            Path to the google_api_token json file.
        
        scopes: list
            Scopes of the api token.
        """
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, scopes)
        else: return None

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else : return None
        return creds
    