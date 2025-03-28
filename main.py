from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import api_hash, api_id
from os_funcs import get_files_formats, rename_all

client = TelegramClient('me', api_id, api_hash)

async def delete_all():
    await client.start()

    photos = await client.get_profile_photos('me')
    if photos:
        await client(DeletePhotosRequest(photos))
        print("фотографии удалены")

    pass

async def add_avatar(file_name):
    await client.start()

    file = await client.upload_file(f'your_images/{file_name}')

    await client(UploadProfilePhotoRequest(file=file))

    print("фотография добавлена")
    
    pass

async def main():
    try:
        rename_all()
        for i in range(len(get_files_formats())):
            await add_avatar(f'{i}.{get_files_formats()[i]}') 
    except Exception as e:
        print(e)

if __name__ == '__main__':
    with client:
        print("хотите удалить все прошлые фотографии? y/n")
        choise = input()
        if choise == 'y' or choise == 'Y':
            client.loop.run_until_complete(delete_all())
        client.loop.run_until_complete(main())