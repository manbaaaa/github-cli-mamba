import os

import requests


def get_all_user_repositories(username: str):
    base_url = f"https://api.github.com/users/{username}/repos"

    repos = []
    if os.environ.get("GITHUB_TOKEN"):
        headers = {"Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}"}
    else:
        headers = {}

    try:
        page = 1
        while True:
            params = {"page": page, "per_page": 10}
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            repositories = response.json()

            if not repositories:
                break

            for repo in repositories:
                repo_info = {
                    "id": repo.get("id", 0),
                    "name": repo.get("name", ""),
                    "url": repo.get("html_url", ""),
                    "description": repo.get("description", ""),
                    "language": repo.get("language", ""),
                    "stars": repo.get("stargazers_count", 0),
                    "forks": repo.get("forks_count", 0),
                    "fork": str(repo.get("fork", False)),
                    "created_at": repo.get("created_at", ""),
                }
                repos.append(repo_info)
            page += 1
        return repos

    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories for {username}: {e}")
        return []
