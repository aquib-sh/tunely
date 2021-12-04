import config
from services.google.token import TokenGenerator

generator = TokenGenerator()

token = generator.generate_google_api_token(
            config.google_client_secret_path, 
            config.google_api_scope
        )
generator.export_token(token, config.google_api_token_path)
