import os

import typer
from dotenv import load_dotenv
from github import get_all_user_repositories
from options import OutputOption
from rich import print
from utils import print_beautify

if os.path.exists(".env"):
    load_dotenv()


app = typer.Typer()
repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


@repo_app.command(name="list", help="List all repositories for a user")
def list_repos(
    user: str = typer.Option(
        ..., "--user", "-u", help="The username to list repositories for"
    ),
    output: OutputOption = typer.Option(
        OutputOption.json, "--output", "-o", help="The output format"
    ),
):
    repos = get_all_user_repositories(user)
    print_beautify(repos, output)


if __name__ == "__main__":
    app()
