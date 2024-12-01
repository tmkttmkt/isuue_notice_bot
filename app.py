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
def hello_world():
  bot.run(os.getenv("DISCORD_TOKEN"))
  return 'start'
@app.route('/stop')
def hello_world():
  bot.close()
  return 'stop'


if __name__ == "__main__":
   app.run(debug=True, use_reloader=False)