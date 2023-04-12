import re
import base64
from github import Github

def scan_for_api_keys(content):
    # Example pattern for API keys, adjust this regex pattern as needed
    api_key_pattern = re.compile(r'[A-Za-z0-9]{32,}')
    return re.findall(api_key_pattern, content)

def main():
    github_token = 'your_github_token'
    g = Github(github_token)
    user = g.get_user()

    for repo in user.get_repos():
        print(f'Scanning repository: {repo.name}')

        try:
            for file in repo.get_contents(''):
                if file.type == 'file':
                    content = base64.b64decode(file.content).decode('utf-8')
                    keys = scan_for_api_keys(content)

                    if keys:
                        print(f'  - Found potential API keys in {file.name}: {keys}')
                else:
                    print(f'  - Skipping {file.name} (not a file)')

        except Exception as e:
            print(f'  - Error scanning {repo.name}: {e}')

if __name__ == '__main__':
    main()

A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8S9t0U1v2W3x4