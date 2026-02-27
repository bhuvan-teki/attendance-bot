import discord
from discord.ext import commands
import aiocron
import os
from flask import Flask
from threading import Thread

# 1. Tiny Web Server to keep Render happy
app = Flask('')
@app.route('/')
def home(): return "I am alive!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

# 2. Discord Bot Setup
TOKEN = os.getenv('MTQ3NjgxOTY5NjE4NjU1NjU1Nw.GSwkx0.VeFBq6s3Z78RRpqONtnbb7ihLAiF7qySk6Ce6Y')
CHANNEL_ID = 1476817434160926858 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# THE SCHEDULES (IST converted to UTC)
@aiocron.crontab('30 03 * * *') # 9:00 AM IST
async def t1(): await bot.get_channel(CHANNEL_ID).send("Attendance 9:00 AM")
# ... add your other @aiocron times here ...

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

# 3. Start both
Thread(target=run_web).start()
bot.run(TOKEN)