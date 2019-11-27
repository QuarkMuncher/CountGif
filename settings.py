from dotenv import load_dotenv
from pathlib import Path
from os import getenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

GIF_FOLDER = getenv("GIF_FOLDER")
