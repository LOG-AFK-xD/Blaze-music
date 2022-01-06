# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**☞ ✰Hᴇʟʟᴏ.. ❣ {message.from_user.mention()} ❣ !**\n
**☞ ✰Iᴍ..[➖ ⃟💫🇧ʟᴀᴢᴇ ✘🇲ᴜsɪᴄ ‌‌ﮩ٨ـ 🎧ﮩ٨ـ](https://t.me/Blaze_Music_bot)**
**☞ ✰Tʜɪs ɪs Vɪᴅᴇᴏ + Mᴜsɪᴄ🎶 RᴏBᴏᴛ ..**
**☞ 📢 𝗣ᴏᴡᴇʀᴇᴅ 𝗕ʏ :- [Bʟᴀᴢᴇ](https://t.me/THE_BLAZE_NETWORK)!**
**☞ ✰Fᴏʀ Mᴏʀᴇ Hᴇʟᴘ Usᴇ Bᴜᴛᴛᴏɴs Bᴇʟᴏᴡ Aɴᴅ Aʙᴏᴜᴛ Aʟʟ Fᴇᴀᴛᴜʀᴇ Oғ Tʜɪs Bᴏᴛ, Jᴜsᴛ Tyᴘᴇ /help**
""",
    reply_markup=InlineKeyboardMarkup(
       [
          [
             
                  InlineKeyboardButton("🔐 𝗖ᴏᴍᴍᴀɴᴅꜱ", callback_data="cbcmds"),
                  InlineKeyboardButton("𝗕ᴀ𝘀ɪᴄ 𝗚ᴜɪᴅᴇ🔰", callback_data="cbhowtouse")
              ],
              [
                  InlineKeyboardButton(
                      "✨𝗗ᴇᴠᴇʟᴏᴘ𝗲𝗿", url=f"https://t.me/log_afk"
                  ),
                  InlineKeyboardButton(
                      "𝗗ᴇᴠᴇʟᴏᴘ𝗲𝗿 Ⅱ💠", url=f"https://t.me/Evil_xD_boy"
                  ),
              ],
              [
                  InlineKeyboardButton(
                      "⚙️ 𝐒ᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/Blaze_Support"
                  ),
                  InlineKeyboardButton(
                      "𝐔ᴘᴅᴀᴛᴇ𝘀 🏜️", url=f"https://t.me/all_Dear_comrade"
              ),
          ],
          [
              InlineKeyboardButton(
                  "🎇 𝐂ʜᴀᴛ 𝐙ᴏɴᴇ", url=f"https://t.me/UNIQUE_SOCIETY"
              ),
              InlineKeyboardButton(
                    "𝐅ɪɢʜᴛɪɴɢ 𝐂ʟᴜʙ✨", url=f"https://t.me/THE_BLAZE_FIGHTER"
             )
          ],
      ]
   ),
   disable_web_page_preview=True,
)

@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /mplay (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
