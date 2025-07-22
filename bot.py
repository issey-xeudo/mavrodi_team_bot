from aiogram import Bot, Dispatcher, executor, types
import qrcode
from io import BytesIO

API_TOKEN = '8179686973:AAFP5po5GJW4mK1pfX4Yy9wLj6Axb1OMTcM'
OWNER_USERNAME = 'Akuma_hkmv'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = (
        "Привет, мой юный друг...\n"
        "Я глава клана Mavrodi, и мой псевдоним — тату.\n\n"
        "Наша команда кибер‑аналитиков считается клинком правосудия.\n"
        "Мы — клан белых хакеров, занимаемся гигиеной сетей и очисткой вредоносного ПО.\n"
        "Вкратце: мы — санитары паутины.\n\n"
        "Если есть вопросы или предложения — я сразу отвечу."
    )
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🧠 Задать вопрос", url=f"https://t.me/{OWNER_USERNAME}"))
    kb.add(types.InlineKeyboardButton("📦 Создать QR", callback_data="make_qr"))
    await message.answer(text, reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data == 'make_qr')
async def qr_request(call: types.CallbackQuery):
    await call.answer("Отправь текст или ссылку — я создам QR‑код.")
    dp.register_message_handler(generate_qr, state=None)

async def generate_qr(message: types.Message):
    text = message.text
    img = qrcode.make(text)
    bio = BytesIO()
    img.save(bio, 'PNG')
    bio.name = 'qr.png'
    bio.seek(0)
    caption = "Создан Mavrodi_Team, главой клана ТАТУ"
    await message.reply_photo(photo=bio, caption=caption)
    dp.unregister_message_handler(generate_qr)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
