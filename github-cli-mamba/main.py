import os

import typer
from cli.repo import repo_app
from cli.user import user_app
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()


app = typer.Typer()


app.add_typer(repo_app, name="repo", help="github repository commands")
app.add_typer(user_app, name="user", help="github user commands")

if __name__ == "__main__":
    app()
