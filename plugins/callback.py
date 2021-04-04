#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from sample_config import Config
from script import script


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


    elif query.data == "download_file":
        await query.answer()
        await query.message.delete()
        await download_file(client, query.message)


    elif query.data == "close": 
        await query.message.delete()  
        await query.answer(
                "Cancelled...",
                show_alert=True
            ) 
        except:
            await query.answer() 
            await query.message.edit_text(" ")        
