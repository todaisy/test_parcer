from telethon import TelegramClient
import time

api_id = 000
api_hash = '476474647545ddfghdfgd'
client = TelegramClient('test_tg', api_id, api_hash)


async def main():
    me = await client.get_me()
    dialogs = await client.get_dialogs()
    # print(me)
    # print(len(dialogs))

    for dialog in dialogs:
        if dialog.title == 'свята':
            print('Find!')
            messages = client.iter_messages(dialog)
            async for message in messages:
                print(message.text)
                time.sleep(1)

# message.date -- Содержит дату сообщения
# message.edit_date -- Содержит дату редактирования сообщения
# message.file -- Содержит файл, который приложен к сообщению
# message.download_media() -- Позволяет загрузить файл, приложенный к сообщению
# message.is_reply -- Показывает, является ли сообщение ответом на другое сообщение
# message.forward -- Содержит информацию о первоисточнике, если текущее сообщение было переслано

with client:
    # запуск в режиме “пока есть хоть одна работающая функция внутри”:
    client.loop.run_until_complete(main())
