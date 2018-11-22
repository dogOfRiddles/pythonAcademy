from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 322480
api_hash = '3cf434b3393e0db93d9e007c30fc2f23'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

me = client.get_me()
print(me.stringify())

#client.send_message('House_catwife','')
client.disconnect()
