import discord
from discord.ext import commands
import aiocron
import os
from flask import Flask
from threading import Thread

# 1. Tiny Web Server to keep Render "awake"
app = Flask('')
@app.route('/')
def home(): return "Attendance Bot is Online!"

def run_web():
    # Render uses port 10000 by default for web services
    app.run(host='0.0.0.0', port=10000)

# 2. Discord Bot Setup
# We use os.getenv so GitHub doesn't block your push for having a secret token
TOKEN = os.getenv('MTQ3NjgxOTY5NjE4NjU1NjU1Nw.GSTHaw.tvqkv7mZV0QO3Si0np64RrnMkeErc__PCcoGcs') 
CHANNEL_ID = 1476817434160926858  # Your Integrated Channel ID

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# THE SCHEDULES (IST times converted to UTC for the server)
@aiocron.crontab('30 03 * * *') # 9:00 AM IST
async def t1(): await bot.get_channel(CHANNEL_ID).send("Attendance 9:00 AM @everyone")

@aiocron.crontab('20 04 * * *') # 9:50 AM IST
async def t2(): await bot.get_channel(CHANNEL_ID).send("Attendance 9:50 AM @everyone")

@aiocron.crontab('10 05 * * *') # 10:40 AM IST
async def t3(): await bot.get_channel(CHANNEL_ID).send("Attendance 10:40 AM @everyone")

@aiocron.crontab('00 06 * * *') # 11:30 AM IST
async def t4(): await bot.get_channel(CHANNEL_ID).send("Attendance 11:30 AM @everyone")

@aiocron.crontab('40 07 * * *') # 1:10 PM IST
async def t5(): await bot.get_channel(CHANNEL_ID).send("Attendance 1:10 PM @everyone")

@aiocron.crontab('30 08 * * *') # 2:00 PM IST
async def t6(): await bot.get_channel(CHANNEL_ID).send("Attendance 2:00 PM @everyone")

@aiocron.crontab('20 09 * * *') # 2:50 PM IST
async def t7(): await bot.get_channel(CHANNEL_ID).send("Attendance 2:50 PM @everyone")

@aiocron.crontab('10 10 * * *') # 3:40 PM IST
async def t8(): await bot.get_channel(CHANNEL_ID).send("Attendance 3:40 PM @everyone")

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

# 3. Start both the Web Server and the Bot
if __name__ == "__main__":
    Thread(target=run_web).start()
    bot.run(TOKEN)