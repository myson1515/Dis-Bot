from flask import Flask
from discord.ext import commands
import os
import asyncio
import discord
app = Flask(__name__)

bot = commands.Bot(command_prefix='prefix', description='Chatterbox')
@bot.event
async def on_message(message):
    mesString = message.content
    fileToWrite = open("transfer.txt", "w")
    mesStringFinal = mesString[8:]
    fileToWrite.write(mesStringFinal)
    fileToWrite.close()
    os.system("python2 readToFile.py")

    fileToOpen = open("transfer.txt").read()
    text = fileToOpen
    channel = message.channel
    if message.content.startswith("!cgsbot"): await bot.send_message(channel, text)

bot.run('MzYzNDY2Njg2MTMwODE0OTg3.DNEpwg.J9xWSLkaiqOerH1CiZDQgu7ktYA')

@app.router('/')
def index():
   return("OK!")
if __name__ == "__main__":
   app.run 

