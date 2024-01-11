# TweetTokFixer

Discord bot that fixes broken Twitter/X embeds, as well as TikTok embeds (who the fuck wants to solve a captcha to watch a 6 second video?)

Originally was going to use yt-dlp to extract the video files and re-serve them on a web server, but fxtwitter and vxtiktok already exist and do a good job. If those ever go down, I'll reapproach the web server.

# How to Install

1. Make a Discord bot on the developer portal and get your bot token
2. `pip install discord.py urlextract`
3. Run discord_bot.py with your new token
4. If you want, build it into a docker image and use docker run or docker-compose to keep it running forever :)
