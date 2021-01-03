import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import time
import os
import sqlite3
import asyncio

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import script

import pyrogram

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant

from plugins.rename_file import rename_doc


@Client.on_message(filters.command(["help"]))
def help_user(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=script.HELP_USER,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Creator", url='https://t.me/AswanthVK'),
                                                InlineKeyboardButton(text="Close", callback_data="cancel_e")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["start"]))
def send_start(bot, update):
    # logger.info(update)
    
    bot.send_message(
        chat_id=update.chat.id,
        text=script.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Project Channel", url="https://t.me/TheSuperBots")],
                                           [InlineKeyboardButton(text="Creator", url="https://t.me/AswanthVK"),
                                                InlineKeyboardButton(text="Close", callback_data="cancel_e")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["upgrade"]))
def upgrade(bot, update):
    # logger.info(update)

    bot.send_message(
        chat_id=update.chat.id,
        text=script.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

    
@Client.on_message(filters.command(["about"]))
def upgrade(bot, update):
    # logger.info(update)

    bot.send_message(
        chat_id=update.chat.id,
        text=script.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@Client.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.voice | filters.video_note))
async def rename_cb(bot, update):
 
    file = update.document or update.video or update.audio or update.voice or update.video_note
    try:
        filename = file.file_name
    except:
        filename = "Not Available"  
    elif (tldextract.extract(m.text)).domain not in youtube_dl_links:
            file_size = header_info.get("Content-Length") if "Content-Length" in header_info else None
            if file_size is not None and int(file_size) > 2147483648:
                await m.reply_text(
                    f"Well that file is bigger than I can upload to telegram!"
                )
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="<b>File Name</b> : <code>{}</code> \n\nSelect the desired option below 👇".format(filename),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📝Rename", callback_data="rename_button"),
                                                InlineKeyboardButton(text="✖Cancel", callback_data="cancel_e")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    )   


async def cancel_extract(bot, update):
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="",
    )
