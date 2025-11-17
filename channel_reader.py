import os
from telethon import TelegramClient, events, utils
import asyncio
from datetime import datetime  

api_id = 0    
api_hash = '0' 
chat_link = '0' 
client = TelegramClient('session', api_id, api_hash)

os.makedirs("logs", exist_ok=True)
log_file = "logs/messages.txt"

async def main():
    await client.start()

    chat = await client.get_entity(chat_link)
    print(f"Чтение чата: {chat.title}")

    @client.on(events.NewMessage(chats=chat))
    async def handler(event):
        msg = event.message

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sender = await msg.get_sender()
        sender_name = sender.first_name if sender else "Неизвестно"

        text = msg.message or ""

        block = (
            f"[{time}] {sender_name}:\n"
            f"{text}\n"
            "----------------------------------------\n"
        )

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(block)

        print(block)

    print("Ожидаю сообщения...")
    await client.run_until_disconnected()

asyncio.run(main())