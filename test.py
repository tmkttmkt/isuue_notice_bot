import requests
import json
# GitHubのAPIエンドポイント
repo_owner = "tmkttmkt"  # リポジトリの所有者（ユーザー名または組織名）
repo_name = "HakkasonD2"  # リポジトリ名
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

# イシューを取得
response = requests.get(url)

# ステータスコードが200の場合はイシュー情報を表示
if response.status_code == 200:
    issues = response.json()
    for issue in issues:
        assignees=[assigne["login"] for assigne in issue["assignees"]]
else:
    print(f"Failed to retrieve issues: {response.status_code}")
