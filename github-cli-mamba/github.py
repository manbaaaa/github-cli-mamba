import os

import requests


class GithubAPI:
    def __init__(self, username: str):
        if os.environ.get("GITHUB_TOKEN"):
            self.headers = {"Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}"}
        else:
            self.headers = {}

    def delete_repository_for_user(self, username: str, repo_name: str):
        base_url = f"https://api.github.com/repos/{username}/{repo_name}"
        response = requests.delete(base_url, headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            return False

    def get_all_user_repositories(self, username: str):
        base_url = f"https://api.github.com/users/{username}/repos"

        repos = []

        try:
            page = 1
            while True:
                params = {"page": page, "per_page": 10}
                response = requests.get(base_url, headers=self.headers, params=params)
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
