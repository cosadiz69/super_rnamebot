#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import pyrogram
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from sample_config import Config
from script import script

from plugins.help_text import rename_cb, cancel_extract
from plugins.rename_file import force_name

@Client.on_callback_query()
async def cb_handler(client, query):

    if query.data == "start_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Project Channel", url="https://t.me/TheSuperBots")],
            [InlineKeyboardButton("Help", callback_data="help_data"),
                 InlineKeyboardButton("Creator", url="https://t.me/AswanthVK")]
        ])

        await query.message.edit_text(
            script.START_TEXT.format(query.from_user.mention),
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return


    elif query.data == "help_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("About", callback_data="about_data"),
                 InlineKeyboardButton("Close", callback_data="cancel_e")]
        ])

        await query.message.edit_text(
            script.HELP_USER,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return


    elif query.data == "about_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Close", callback_data="cancel_e")]
        ])

        await query.message.edit_text(
            Script.ABOUT_TEXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    
@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_button" in update.data:
        await update.message.delete()
        await force_name(bot, update.message)
        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)
