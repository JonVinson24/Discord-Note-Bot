import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)


@client.command()
@commands.has_role("team_3")
async def note(ctx, *, message: str):
    with open("../../../Desktop/notes.txt", "a") as f:
        f.write("- " + message + "\n")
    await ctx.send("Note added!")


@client.command()
@commands.has_role("team_3")
async def log(ctx):
    with open("../../../Desktop/notes.txt", "r") as f:
        notes = f.read()
    await ctx.send("```" + notes + "```")


@client.command()
@commands.has_role("team_3")
async def remove_last(ctx):
    with open("../../../Desktop/notes.txt", "r") as f:
        lines = f.readlines()
    if lines:
        last_line = lines[-1]
        lines = lines[:-1]
    else:
        await ctx.send("The note file is empty.")
        return
    with open("../../../Desktop/notes.txt", "w") as f:
        f.writelines(lines)
    await ctx.send(f"Note '{last_line.strip()}' was removed")


@client.command()
@commands.has_role("team_3")
async def clear_all(ctx):
    with open("../../../Desktop/notes.txt", "w") as f:
        f.write("")
    await ctx.send("All notes have been cleared.")


client.run(token)
