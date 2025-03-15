import typer
from github import get_all_user_repositories
from rich import print

app = typer.Typer()
repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


@repo_app.command(name="list", help="List all repositories for a user")
def list_repos(
    user: str = typer.Option(
        ..., "--user", "-u", help="The username to list repositories for"
    )
):
    repos = get_all_user_repositories(user)
    for repo in repos:
        print(repo)


if __name__ == "__main__":
    app()
