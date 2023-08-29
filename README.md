# Bingus Bot

Bingus Bot is a simple Discord bot built using the Discord API and the discord.py library. It can perform various actions in a Discord server, including sending messages, joining voice channels, playing audio, and more.

## Features

- Responds to commands like `!hello` and `!daniel` with custom messages.
- Welcomes new members to the server with a message in a designated channel.
- Can join a voice channel using the `!join` command and play audio using the `!play` command.
- Supports pausing, resuming, and stopping audio playback in a voice channel.

## Prerequisites

- Python 3.6 or higher
- discord.py library
- FFmpeg for audio playback (required by FFmpegPCMAudio)

## Usage

- Invite the bot to your Discord server and grant necessary permissions.
- Use commands like `!hello` and `!join` in text channels to interact with the bot.
- Use the `!play` command to make the bot join a voice channel and play audio.
- To play an audio file, import any ".wav" file to the folder.

## Configuration

Modify the `.env` file to configure your bot:

- `DISCORD_TOKEN`: Your Discord bot token.
- `WELCOME_CHANNEL_ID`: The ID of the channel where new member welcome messages will be sent.
