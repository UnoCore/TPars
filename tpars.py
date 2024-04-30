from telethon import TelegramClient, sync, events
from discord_webhook import DiscordWebhook
import os
from translate import Translator

os.system('cls')
os.system('title TPars')

webhooks = [
    'https://discord.com/api/webhooks/1080470684079231006/usZW9YRn7tya0PvIVKVyTGyAAAmKnKgKsTpZPoZRU0wAm_eYKrI0Wnl8hsJnyJK3fDzq',
    'https://discord.com/api/webhooks/1080470481087516733/w_4AvaSOXqZwx0mXaDcPL0G4r6QETA0qFGKn9JtrDKbHKlFFjsPAwD2mXQxIYIeIwuz1',
    'https://discord.com/api/webhooks/1069336217033916466/S1CtrdaxmWCJ0fe7bHNI3y9JUMFkptE41QKbuuAqJgZZ4BNuJtOpqQ2thUQk-dsrd4D4'
]

client = TelegramClient('Stats', api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=('Rflive'))) ### RFLIVE
async def normal_handler(event):
    translator = Translator(from_lang="en", to_lang="ru")
    result = translator.translate(event.message.to_dict()['message'])
    message = result
    webhook = DiscordWebhook(
        url=webhooks[0],
        content=message)
    response = webhook.execute()
    print(f'[+] News from @Rfilve published!\n')

@client.on(events.NewMessage(chats=('transferyi'))) ### TRANSFERYI
async def normal_handler(event):
    translator = Translator(from_lang="en", to_lang="ru")
    result = translator.translate(event.message.to_dict()['message'])
    message = result
    webhook = DiscordWebhook(
        url=webhooks[1],
        content=message)
    response = webhook.execute()
    print(f'[+] News from @Transferyi published!\n')

@client.on(events.NewMessage(chats=('Fabrizio'))) ### FABRIZIO
async def normal_handler(event):
    translator = Translator(from_lang="en", to_lang="ru")
    result = translator.translate(event.message.to_dict()['message'])
    message = result
    webhook = DiscordWebhook(
        url=webhooks[2],
        content=message)
    response = webhook.execute()
    print(f'[+] News from @Fabrizio published!\n')

os.system('cls')
print(f"[+] Logged in!")
print(f"\n[+] Waiting for news..\n\n")

client.run_until_disconnected()
