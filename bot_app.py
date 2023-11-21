import asyncio

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.token_bot import TOKEN
from utils.convert_to_mp3 import convert_to_mp3
from utils.keyboards import get_kb
from ML_model import speech_rec

response = '''Привет, я бот конвертирующий аудиосообщения в текст.
Для работы я использую ML-модели. 
Чем больше модель тем дольше ждать обработки, и тем лучше будет результат. 
Отправь мне аудио и выбери модель.
'''

models = ['tiny', 'base', 'small', 'medium', 'large']


bot = Bot(TOKEN, parse_mode='html')
dp = Dispatcher()



# обработка команды start
@dp.message(CommandStart())
async def cmd_start_hdl(msg: Message) -> None:
    await msg.answer(response)



# обработка и конвертация аудио, отправка клавиатуры с выбором модели
@dp.message(F.audio)
async def download_audio(msg: Message, bot: Bot) -> None:
    await bot.download(file=msg.audio, destination='media/audio.ogg')
    convert_to_mp3()
    await msg.answer("Выберите модель", reply_markup=get_kb())



# обработка и конвертация голоса, отправка клавиатуры с выбором модели
@dp.message(F.voice)
async def download_voice(msg: Message, bot: Bot) -> None:
    await bot.download(file=msg.voice, destination='media/audio.ogg')
    convert_to_mp3()
    await msg.answer("Выберите модель", reply_markup=get_kb())



# запуск распознования аудио, после выбора модели
@dp.message(F.text.in_(models))
async def start_recognizing(msg: Message) -> None:
    await msg.answer("Обработка...", reply_markup=types.ReplyKeyboardRemove())
    await msg.answer(speech_rec(model=msg.text))



# запсук прослушивания апдейтов
async def main() -> None:
    await dp.start_polling(bot)


# запуск программы
if __name__ == '__main__':
    asyncio.run(main())