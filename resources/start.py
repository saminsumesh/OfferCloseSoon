from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def cmd_start(client: Client, message):
      pp=await message.reply_sticker(
            sticker = "CAACAgUAAxkBAAECSC5iWtY31mtvT4ykobd0N4tw9ZmR_wACRwIAAlJa9jtj_y8Dm5CUrB4E")    
      await asyncio.sleep(25)    
      await pp.delete()  
            
