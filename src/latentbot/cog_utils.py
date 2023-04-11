from pathlib import Path


def load_cogs(bot, cwd: Path):
    cogs_path = cwd / "cogs"

    for cog_dir in cogs_path.iterdir():
        if cog_dir.is_dir():
            init_file = cog_dir / "__init__.py"
            if init_file.exists():
                cog_name = f"latentbot.cogs.{cog_dir.name}"
                print(f"Loading cog '{cog_name}'")
                bot.load_extension(cog_name)
