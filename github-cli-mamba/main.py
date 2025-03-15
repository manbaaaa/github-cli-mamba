import os

import jmespath
import typer
from dotenv import load_dotenv
from github import get_all_user_repositories
from options import OutputOption
from rich import print
from utils import print_beautify, sort_by_field

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
    query: str = typer.Option(None, "--query", "-q", help="query with jmespath"),
    sort: str = typer.Option(None, "--sort", "-s", help="sort by field"),
):
    repos = get_all_user_repositories(user)
    if query:
        # filter query: "[?language == 'Python' && description != None && contains(description, 'Python')]"
        # sort query: "sort_by(@, &stars).reverse(@)"
        # filter and sort query: "sort_by([?language == 'Python'], &stars).reverse(@)"
        repos = jmespath.search(query, repos)
    if sort:
        if sort.startswith("~"):
            reverse = True
            sort = sort[1:].split(",")
        else:
            reverse = False
        repos = sort_by_field(repos, sort, reverse)
    print_beautify(repos, output)


if __name__ == "__main__":
    app()
