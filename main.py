from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio
from aiogram.types import ReplyKeyboardRemove
from default_keyboard import main_keyboard
from inline_keyboard import about_inline_keyboard, photo_inline_keyboard, media_inline_keyboard

API_TOKEN = "8356470658:AAH5-fD8pEf9RhfMC_VkC2Eo3zq6OVlvIB4"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
photo = "https://i.scdn.co/image/ab67616d0000b2735cb651c4b651a080f3cdae9f"


@dp.message(Command('start'))
async def send_message(message: types.Message):
    await message.answer("Salom Sultan Vilgelm Abob II haqida botga xush kelibsiz",
                         reply_markup=main_keyboard())


@dp.message(F.text == "About me")
async def send_message(message: types.Message):
    await message.answer(text="About me",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Sultan Vilgelm Abob II haqimda ma'lumot",
                         reply_markup=about_inline_keyboard())


@dp.message(F.text == "Media url")
async def send_message(message: types.Message):
    await message.answer(text="Media url",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer("Media",
                         reply_markup=media_inline_keyboard())


# inline  ------------------------------------------------------------------------------


@dp.callback_query(F.data == "fullname")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer(text="Sultan Vilgelm Abob II")


@dp.callback_query(F.data == "job")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer(text="Hacker")

@dp.callback_query(F.data == "back")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer(text="Ortga",
                                  reply_markup=main_keyboard())
    await callback.message.delete()


@dp.callback_query(F.data == "photo")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo=photo,
                                        reply_markup=photo_inline_keyboard())
    await callback.message.delete()


clicked = False
@dp.callback_query(F.data == "like")
async def send_message(callback: types.CallbackQuery):
    global clicked
    if clicked == False:
        await callback.answer("Siz like bosdingiz")
        clicked = True
    elif clicked == True:
        await callback.answer("Siz like ni qaytarib oldindiz(ayayay papayay, laykni qayta bos",
                              show_alert=True)
        clicked = False

clicked = False
@dp.callback_query(F.data == "dislike")
async def send_message(callback: types.CallbackQuery):
    global clicked
    if clicked == False:
        await callback.answer("Siz dislike bosdingiz(aayayay papayay, man sani ДОКС qilaman)")
        clicked = True
    elif clicked == True:
        await callback.answer("Siz dislike ni qaytarib oldindiz(malades, endi laykni bos)",
                              show_alert=True)
        clicked = False

@dp.callback_query(F.data == "back2")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer(text="Ortga",
                                  reply_markup=about_inline_keyboard())
    await callback.message.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
