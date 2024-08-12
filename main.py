import requests
import json
from github import Github
from keys import NOTION_API_KEY, NOTION_PAGE, NOTION_URL, NOTION_VERSION, GIT_FILE_PATH, GIT_REPO, GIT_TOKEN

def get_notion_page_content():
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
    }
    response = requests.get(NOTION_URL, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch Notion data. Status code: {response.status_code}")
        print("Response text:", response.text)
        return None
    return response.json()

def convert_to_markdown(notion_data):
    markdown_content = ""
    for block in notion_data['results']:
        if block['type'] == 'child_page':
            title = block['child_page']['title']
            page_url = f"https://www.notion.so/{block['id'].replace('-', '')}"
            markdown_content += f"- [{title}]({page_url})\n"
        # 他のタイプのブロックも必要に応じて処理
    return markdown_content

def upload_to_github(content):
    g = Github(GIT_TOKEN)
    repo = g.get_repo(GIT_REPO)
    
    try:
        contents = repo.get_contents(GIT_FILE_PATH, ref="main")
        repo.update_file(GIT_FILE_PATH, "Update file with Notion data", content, contents.sha, branch="main")
    except:
        repo.create_file(GIT_FILE_PATH, "Initial commit with Notion data", content, branch="main")

def main():
    notion_data = get_notion_page_content()
    if notion_data:
        markdown_content = convert_to_markdown(notion_data)
        upload_to_github(markdown_content)
        print("File updated successfully.")

if __name__ == "__main__":
    main()