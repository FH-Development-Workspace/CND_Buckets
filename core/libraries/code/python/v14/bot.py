import os
import asyncio

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from api import create_license, FHAPIError


load_dotenv()


intents = discord.Intents.default()


bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)


# ============================================================
# LOAD COMMANDS
# ============================================================

async def load_commands():
    """
    Automatically load every command cog from the cmds/
    directory.
    """

    for filename in os.listdir("cmds"):
        if filename.startswith("_"):
            continue

        if not filename.endswith(".py"):
            continue

        extension = f"cmds.{filename[:-3]}"

        try:
            await bot.load_extension(extension)
            print(f"Loaded command extension: {extension}")

        except Exception as error:
            print(
                f"Failed to load command extension "
                f"{extension}: {type(error).__name__}: {error}"
            )


# ============================================================
# BOT READY
# ============================================================

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("FH Developments bot is online.")

    try:
        synced = await bot.tree.sync()

        print(
            f"Synced {len(synced)} application command(s)."
        )

    except Exception as error:
        print(
            f"Failed to sync application commands: {error}"
        )


# ============================================================
# /license-create
# ============================================================

@bot.tree.command(
    name="license-create",
    description="Create an FH Developments license.",
)
@app_commands.describe(
    discord_id="Discord ID of the customer.",
    roblox_id="Roblox ID of the customer.",
    product_id="Product ID.",
    expires_at="Expiry date in ISO format, or leave empty.",
    file_id="File ID to assign to the license.",
)
async def license_create(
    interaction: discord.Interaction,
    discord_id: str,
    roblox_id: str,
    product_id: str,
    expires_at: str | None = None,
    file_id: int | None = None,
):
    await interaction.response.defer(
        ephemeral=True
    )

    try:
        license_data = await create_license(
            discord_id=discord_id,
            roblox_id=roblox_id,
            product_id=product_id,
            expires_at=expires_at,
            file_id=file_id,
        )

    except FHAPIError as error:
        await interaction.followup.send(
            (
                "❌ **Failed to create license.**\n\n"
                f"API status: `{error.status_code}`\n"
                f"Response: `{error.detail}`"
            ),
            ephemeral=True,
        )

        return

    except Exception as error:
        print(
            f"Unexpected error type: {type(error).__name__}"
        )
        print(
            f"Unexpected error: {error!r}"
        )

        await interaction.followup.send(
            (
                "❌ **An unexpected error occurred.**\n\n"
                f"Error: `{type(error).__name__}: {error}`"
            ),
            ephemeral=True,
        )

        return

    embed = discord.Embed(
        title="FH Developments — License Created",
        description="The license has been successfully created.",
        color=discord.Color.green(),
    )

    embed.add_field(
        name="License UUID",
        value=f"`{license_data['uuid']}`",
        inline=False,
    )

    embed.add_field(
        name="Discord ID",
        value=f"`{license_data['discord_id']}`",
        inline=True,
    )

    embed.add_field(
        name="Roblox ID",
        value=f"`{license_data['roblox_id']}`",
        inline=True,
    )

    embed.add_field(
        name="Product",
        value=f"`{license_data['product_id']}`",
        inline=True,
    )

    embed.add_field(
        name="File ID",
        value=f"`{license_data.get('file_id')}`",
        inline=True,
    )

    embed.add_field(
        name="Active",
        value=f"`{license_data['active']}`",
        inline=True,
    )

    await interaction.followup.send(
        embed=embed,
        ephemeral=True,
    )


# ============================================================
# START BOT
# ============================================================

async def main():
    token = os.getenv("DISCORD_TOKEN")

    if not token:
        raise RuntimeError(
            "DISCORD_TOKEN is missing from .env"
        )

    # Load all cmds/*.py files BEFORE starting the bot.
    await load_commands()

    # Start Discord connection.
    await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
