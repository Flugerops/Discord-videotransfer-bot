from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")

intents = discord.Intents.default()
intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='tiktok')
async def tiktok_video(ctx, tiktok_url):
    try:
        video_url = get_tiktok_video_url(tiktok_url)
        await ctx.send(f'TikTok Video: {video_url}')
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Я сын дерьма')

def get_tiktok_video_url(tiktok_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(tiktok_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    video_tag = soup.find('video')
    if video_tag:
        video_url = video_tag['src']
        return video_url
    else:
        raise Exception('Video not found on the TikTok page')

bot.run(TOKEN)
