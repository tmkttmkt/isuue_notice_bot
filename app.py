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
print(os.environ)
print(DISCORD_TOKEN)
print("DISCORD_TOKEN:", os.getenv("DISCORD_TOKEN"))
# Railway環境変数からトークンを取得
bot.run(os.getenv("DISCORD_TOKEN"))




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
