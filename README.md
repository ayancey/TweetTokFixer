# TweetTokFixer

Discord bot that fixes broken Twitter/X embeds, as well as TikTok embeds (who the fuck wants to solve a captcha to watch a 6 second video?)

Originally was going to use yt-dlp to extract the video files and re-serve them on a web server, but fxtwitter.com and vxtiktok.com already exist and do a good job. If those ever go down, I'll reapproach the web server.

# Screenshots

![image](https://github.com/ayancey/TweetTokFixer/assets/10055792/4f49b324-9320-4ff9-9830-ea0dcc86c183)
![image](https://github.com/ayancey/TweetTokFixer/assets/10055792/42a71eeb-ba50-48a5-be70-aaf0bed3841f)

# How to Install

1. Make a Discord bot on the [developer portal](https://discord.com/developers/applications), go to the Bot section and "Add Bot", and get your bot token.
2. Replace `{PUT YOUR TOKEN HERE}` on the last line of discord_bot.py
3. Run `docker compose up --detach` or `python -m venv venv`, `source venv/bin/activate`, `pip install -r requirements.txt`, `python discord_bot.py`, you know the drill.
