import os
from dotenv import load_dotenv
import requests
load_dotenv()
NOTION_PAGE = os.environ['notion_page']
NOTION_API_KEY = os.environ['notion_api']
NOTION_URL = f"https://api.notion.com/v1/blocks/{NOTION_PAGE}/children"
NOTION_VERSION = '2022-06-28'

GIT_TOKEN = os.environ['git_token']
GIT_REPO = os.environ['git_repo']
GIT_FILE_PATH = 'file.md'

