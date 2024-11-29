from flask import Flask
import discord
import os
import threading
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

# Botの設定
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")




def run_flask():
    app.run(debug=True, use_reloader=False)  # use_reloader=FalseはFlaskの再起動を防ぐ

# Discordボットをメインスレッドで実行
def run_discord_bot():
    bot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    # Flaskをバックグラウンドで実行
    threading.Thread(target=run_flask).start()
    
    # Discordボットを実行
    #threading.Thread(target=run_discord_bot).start()
    run_discord_bot()