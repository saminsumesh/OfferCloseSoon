from pyrogram import Client, filters
from pyrogram.types import (
      Messages,
     # CallBackQuery,
     # InlineKeyboardButton,
     # InlineKeyboardMarkup
)
from time import time

@Client.on_message(filters.command("Client") &filter.group)
async def kick(client: Client, message):
      user_id = message.reply_to_message.from_user.id
      chat_id = int(message.message.chat.id)
      reply_m = message.reply_to_message
      if reply_m:
            user = await get_chat_memeber(message.chat.id, reply_m.from_user.id)
            if user.status not in (("administrator" or "creator")):
                  await message.reply_text("Sorry you're not an admin")
            else:
                  await client.ban_chat_member(chat_id, user_id,  int(time() + 400)
                  await message.reply_text("One has turned into bytes")
                  
