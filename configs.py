import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23171051"))
  API_HASH = os.environ.get("API_HASH", "10331d5d712364f57ffdd23417f4513c")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7076164009:AAHx-pMK8tGnPbhBHtr0ci6Fs-tPehInWd8")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "TMR_File_Store_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002180083054"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "Ziplinker.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "8e869e3bd0f04a3dd1282d4e0a7bb52224a3a576")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6987799874"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://tmr624062:2fS3ifhHtKRaLWQZ@cluster0.3gpzrlg.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001868502293")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002237296986"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""<b>This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟<b>"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Vɪsʜᴀʟ Kᴜᴍᴀʀ](https://t.me/Vishalku25)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Vishalku25)
"""
  HOME_TEXT = """<b>Hɪ, {} 👋 \n\nɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ. ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴅᴏᴄᴜᴍᴇɴᴛ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ & ᴀɴɪᴍᴀᴛɪᴏɴ. ɪ ᴡɪʟʟ ꜱᴛᴏʀᴇ ɪᴛ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜱʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴀᴛ ꜰɪʟᴇ.. \n\n‼️ ᴄʟɪᴄᴋ ᴏɴ Aʙᴏᴜᴛ ᴛᴏ ɢᴇᴛ ғᴜʟʟ ᴅᴇᴛᴀɪʟꜱ ᴏғ ᴀʟʟ ᴍʏ ғᴇᴀᴛᴜʀᴇꜱ . \n\n🧑‍💻 ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/Vishalku25">Vɪsʜᴀʟ Kᴜᴍᴀʀ</a><b>"""
