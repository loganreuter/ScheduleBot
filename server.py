import pickle
import os

import requests
from bs4 import BeautifulSoup
import discord
from dotenv import load_dotenv

"""
IDEA:
- Person sends CRN of class they want to monitor
- Validate that the CRN works by sending a request
- If course is validated, added it to database (using pickle)
- If not validated respond to use the course could not be found
- We then send a new request ever 10 minutes? 30 minutes? or hour?
- Compare number of open seats and waitlist
- If either change send message to discord
"""

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Term codes for each quarter
FQ = 202310
WQ = 202401
SQ = 202403

DELIM = "!"

def add_course(*args):
    pass

def rm_course(*args):
    pass

class ScheduleBot(discord.Client):
    def __init__(self):
        super.__init__(self)
        self.args = {
            "add": add_course,
            "remove": rm_course
        }

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")
    
    async def on_message(self, message: discord.Message):
        for arg in self.args.keys():
            key = f"{DELIM}{arg}"

            if message.content.startswith(key):
                self.args[key]()

bot = ScheduleBot()
bot.run(TOKEN)
