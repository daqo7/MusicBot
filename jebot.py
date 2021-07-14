#    Copyright (c) 2021 DAQO BOTs <https://t.me/daqomods>
 
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from sample_config import Config
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


Jebot = Client(
   "Song Downloader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)


 #For private messages        
 #Ignore commands
 #No bots also allowed
@Jebot.on_message(filters.private & ~filters.bot & ~filters.command("help") & ~filters.command("start") & ~filters.command("s"))
async def song(client, message):
 #dasqin #daqomods
    cap = "Xoş dinləmələr baby."
    url = message.text
    rkp = await message.reply("Biraz gözlə...")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("Bu mahnını tapa bilmədim.")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("Yüklənir...")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`Endirmə məzmunu çox qısadır.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Web sayt tərəfindən qoyulmuş coğrafi məhdudiyyətlər səbəbindən video yüklənə bilmir.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Maksimum yükləmə limitinə çatıldı.`")
        return
    except PostProcessingError:
        await rkp.edit("`Sonrakı işləmə zamanı bir xəta baş verdi.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Tələb olunan formatda media mövcud deyil.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`Məlumat çıxarılması zamanı xəta baş verdi.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("Sizə göndərirəm...") #dasqin
        lol = "./thumb.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)  #daqomods
        await rkp.delete()
        os.system("rm -rf *.mp3")
        os.system("rm -rf *.webp")
  
    
@Jebot.on_message(filters.command("song") & ~filters.edited & filters.group)
async def song(client, message):
    cap = "@daqomods"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("Biraz gözlə...")
    if not url:
        await rkp.edit("**İstədiyiniz mahnı hansıdır?**\nBu şəkildə yaz`/song <mahnı adı>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("Bu mahnını tapa bilmədim.")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("Yüklənir...")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`Endirmə məzmunu çox qısadır.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Web sayt tərəfindən qoyulmuş coğrafi məhdudiyyətlər səbəbindən video yüklənə bilmir.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("Maksimum yükləmə limitinə çatıldı.`")
        return
    except PostProcessingError:
        await rkp.edit("``Sonrakı işləmə zamanı bir xəta baş verdi.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Tələb olunan formatda media mövcud deyil.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`Məlumat çıxarılması zamanı xəta baş verdi.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("Sizə göndərirəm...") #dasqin
        lol = "./thumb.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)  #daqomods
        await rkp.delete()
        os.system("rm -rf *.mp3")
        os.system("rm -rf *.webp")
 
    
@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>SALAM, mən mahnı yükləməyə kömək edən bir botam. Botun müəllifi @daqomods.

Necə işlədiyimi bilmək üçün yardım düyməsinə toxun.</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Yardım", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Kanal", url="https://t.me/daqomods")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html",
            reply_to_message_id=message.message_id
        )
   else:

       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>DAQO Music aktivdir.\n\n</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Yardım", callback_data="help")
                                        
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html",
            reply_to_message_id=message.message_id
        )

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Yükləmək istədiyin mahnının adını yaz.

Powered by @daqomods</b>""",
            reply_to_message_id=message.message_id
        )
    else:
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="<b>Mahnı yükləmək üçün örnək.\n\nBunu yaz: `/song Okaber TABOO</b>",
            reply_to_message_id=message.message_id
        )     
        

@Jebot.on_callback_query()
async def button(Jebot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Jebot, update.message)

print(
    """
Bot Started!

Join @daqomods
"""
)

Jebot.run()
