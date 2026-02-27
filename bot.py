import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
import os

TOKEN = os.getenv("DISCORD_TOKEN")
USER_ID = 1476817434160926858       # friend USER ID (or channel ID if needed)

IST = pytz.timezone("Asia/Kolkata")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

schedule = {
    "09:00": "Attendance 9:00 AM",
    "09:50": "Attendance 9:50 AM",
    "10:40": "Attendance 10:40 AM",
    "11:30": "Attendance 11:30 AM",
    "13:10": "Attendance 1:10 PM",
    "14:00": "Attendance 2:00 PM",
    "14:50": "Attendance 2:50 PM",
    "15:40": "Attendance 3:40 PM",
}

@tasks.loop(minutes=1)
async def attendance_loop():
    now = datetime.now(IST).strftime("%H:%M")
    if now in schedule:
        user = await bot.fetch_user(USER_ID)
        await user.send(schedule[now])

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    attendance_loop.start()

bot.run(TOKEN)