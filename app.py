from flask import Flask
import discord
import os
app = Flask(__name__)


# Botの設定
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")


@app.route('/')
def hello_world():
  return 'Hello, World!'
@app.route('/start')
def start():
  bot.run(os.getenv("DISCORD_TOKEN"))
  return 'start'
@app.route('/stop')
def stop():
  bot.close()
  return 'stop'


if __name__ == "__main__":
   app.run(debug=True, use_reloader=False)

from fastapi import FastAPI
import os
import discord
import asyncio
from threading import Thread

# FastAPIアプリケーションを作成
app = FastAPI()

# Discordクライアントを作成
bot = discord.bot()

@app.on_event("startup")
async def startup_event():
    """FastAPIアプリケーションの起動時にDiscordボットを開始"""
    # Discordボットを非同期で実行
    asyncio.create_task(run_discord_bot())

async def run_discord_bot():
    """非同期でDiscordボットを実行"""
    await bot.start(os.getenv("DISCORD_TOKEN"))

# Discordボットのイベント
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# FastAPIのルート
@app.get("/")
async def read_root():
    return {"message": "Discord bot is running"}

if __name__ == "__main__":
    import uvicorn

    # FastAPIアプリケーションを非同期で起動
    uvicorn.run(app, host="0.0.0.0", port=8000)
