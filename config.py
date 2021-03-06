import os

# ======================= DATABASE FILE  =============================
data_dir = os.path.join(os.getcwd(), "internal")
db_file = "password_manager.db"
db_path = os.path.join(data_dir, db_file)

# ======================= CACHE FILE  =============================
cache_file = "cache.json"
cache_path = os.path.join(data_dir, cache_file)
# ======================= GOOGLE APIs =============================
google_token_file         = 'google_token.json'
google_client_secret_file = 'google_client_secret.json'

google_client_secret_path = os.path.join(data_dir, google_client_secret_file)
google_api_token_path     = os.path.join(data_dir, google_token_file)

google_api_scope = [
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtubepartner",
    "https://www.googleapis.com/auth/youtube.force-ssl" 
]

youtube_channel_id = 'UCKRYP6EAo0n6Notrq7w_2ZA'
fb_group_link = "https://m.facebook.com/groups/923023231097937"
fb_group_announc = "https://m.facebook.com/groups/923023231097937?view=announcements"
