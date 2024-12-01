from fastapi import FastAPI
import os
import discord
import asyncio
from threading import Thread

# FastAPIアプリケーションを作成
app = FastAPI()

# Discordクライアントを作成
bot = discord.Client()

################################################################################################################################################################
async def run_discord_bot():
    """非同期でDiscordボットを実行"""
    await bot.start(os.getenv("DISCORD_TOKEN"))

# Discordボットのイベント
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


################################################################################################################################################################


# FastAPIのルート
@app.get("/")
async def read_root():
    return {"message": "Discord bot is running"}
@app.on_event("startup")
async def startup_event():
    """FastAPIアプリケーションの起動時にDiscordボットを開始"""
    # Discordボットを非同期で実行
    asyncio.create_task(run_discord_bot())

################################################################################################################################################################

if __name__ == "__main__":
    import uvicorn
    # FastAPIアプリケーションを非同期で起動
    uvicorn.run(app, host="0.0.0.0", port=8000)
