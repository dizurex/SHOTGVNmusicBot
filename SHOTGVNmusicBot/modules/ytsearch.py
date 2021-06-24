
import logging

from pyrogram import Client as app
from pyrogram.types import Message
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)


@app.on_message(pyrogram.filters.command(["search"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**/search masukan judul lagu!**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎 **Sedang Mencari lagu...**")
        results = YoutubeSearch(query, max_results=4).to_dict()
        text = ""
        for i in range(4):
            text += f"**Judul  :** `{results[i]['title']}`\n"
            text += f"**Durasi :** {results[i]['duration']}\n"
            text += f"**Penonton :** {results[i]['views']}\n"
            text += f"**Channel :** {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            text += "━━\n"
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
