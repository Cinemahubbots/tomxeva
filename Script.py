class script(object):
    START_TXT = """**ഞാൻ ഒരു 𝐀𝐔𝐓𝐎 𝐅𝐈𝐋𝐓𝐄𝐑 𝐁𝐎𝐓 ആണ്, എന്റെ ഉടമസ്ഥർ  <a href='https://t.me/+79jrN3qvNW5kOTk1'>CINEMA-HUB</a> ആണ്, നിങ്ങൾക്കും നിങ്ങളുടെ ഗ്രൂപ്പുകളിൽ ഇപ്പോൾ എന്നെ ഉപയോഗിക്കാവുന്നതാണ്**"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/BASTINJOE'>Tʜɪs ᴘᴇʀsᴏɴ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://t.me/MYFASTSERVERR'>Qᴜɪᴄᴋ Fᴀsᴛ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.0.3 [ Sᴛᴀʙʟᴇ ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Tom is a private project.   

<b>DEVS:</b>
- <a href=https://t.me/BASTINJOE>BASTIN™</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

-  𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙴𝙻𝚂𝙰 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
