import os

from dotenv import load_dotenv


def load_discord_token() -> str:
    TOKEN = os.getenv("DISCORD_TOKEN")

    if not TOKEN:
        load_dotenv()
        TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise EnvironmentError("No Discord token found in the environment")

    return TOKEN
