from fastapi import FastAPI
import os
import discord
import asyncio
from threading import Thread

# FastAPIアプリケーションを作成
app = FastAPI()

# Discordクライアントを作成
bot = discord.Bot()

################################################################################################################################################################
async def run_discord_bot():
    """非同期でDiscordボットを実行"""
    await bot.start(os.getenv("DISCORD_TOKEN"))
async def stop_discord_bot():
    await bot.close() 
# Discordボットのイベント
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def test(ctx):
    await ctx.respond("かかって来いよ")
################################################################################################################################################################


# FastAPIのルート
@app.get("/")
async def read_root():
    return "hello route"
@app.get("/start")
async def read_root():
    asyncio.create_task(run_discord_bot())
    return "セットアップ"
@app.get("/stop")
async def read_root():
    asyncio.create_task(stop_discord_bot())
    return "ストップダウン"
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_discord_bot())


################################################################################################################################################################

if __name__ == "__main__":
    import uvicorn
    # FastAPIアプリケーションを非同期で起動
    uvicorn.run(app, host="0.0.0.0", port=8000)
