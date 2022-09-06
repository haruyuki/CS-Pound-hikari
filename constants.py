import os


class Constants:
    version = "1.0.0"  # Current version of bot
    prefix = ","  # Prefix used to call bot for commands
    owner_id = 277398425044123649  # User ID of bot owner
    contact_email = "jumpy12359@gmail.com"
    support_link = "https://invite.gg/cspound"  # Link to support server


class Tokens:
    discord_token = os.environ.get("DISCORD_TOKEN", None)  # Discord bot token
    flightrising_token = os.environ.get("FLIGHTRISING_TOKEN", None)  # Flight Rising token
    chickensmoothie_password = os.environ.get("CHICKENSMOOTHIE_PASSWORD", None)  # My ChickenSmoothie
