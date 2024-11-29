from flask import Flask
import discord
import os
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
# Railway環境変数からトークンを取得
bot.run(os.getenv("DISCORD_TOKEN"))




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
