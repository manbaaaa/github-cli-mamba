import os

import typer
from cli.repo import repo_app
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()


app = typer.Typer()


app.add_typer(repo_app, name="repo")


if __name__ == "__main__":
    app()
