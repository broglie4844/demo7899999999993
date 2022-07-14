import os
import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

from pyromod import listen
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from utils import Media
from info import SESSION, APP_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        username = '@t48444844bot'
        print(f"{first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {username}.")

    async def stop(self, *args):
        await super().stop()
        print("Leo Media Search Bot is Stopped Now")


app = Bot()
app.run()
