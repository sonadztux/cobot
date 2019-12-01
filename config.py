import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/Workspaces/cobot/env')
load_dotenv(os.path.join(project_folder, '.config'))

url_api_base        = os.getenv("URL_API_BASE")
product_url_base    = os.getenv("PRODUCT_URL_BASE")
bot_token           = os.getenv("BOT_TOKEN")
chat_id             = os.getenv("CHAT_ID")