import asyncio
import logging

import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    fastapi_host: HttpUrl
    tg_token: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.tg_token)
dp = Dispatcher(storage=MemoryStorage())


class ModelChoice(StatesGroup):
    waiting_for_question = State()

async def get_answer(question: str, model_choice: str) -> str:
    """
    Отправляет запрос к FastAPI для получения ответа.

    Args:
        question: Вопрос пользователя.
        model_choice: Выбранная модель.

    Returns:
        Ответ от FastAPI или сообщение об ошибке.
    """
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{settings.fastapi_host}ask"
            params = {"user_question": question, "model": model_choice}
            async with session.get(url, params=params, timeout=10) as response:
                response.raise_for_status()
                response_data = await response.json()
                return response_data.get("answer", "Ответ не найден")
    except aiohttp.ClientError as e:
        return f"Ошибка при запросе к FastAPI: {e}"
    except Exception as e:
        logging.exception("Произошла непредвиденная ошибка:")
        return f"Бэк еще не проснулся или с ним что-то не так!\n{e}"


async def send_model_selection(message: types.Message, state: FSMContext):
    """Отправляет сообщение с кнопками выбора модели."""
    builder = InlineKeyboardBuilder()
    builder.button(text="ChatGroq", callback_data="ChatGroq")
    builder.button(text="GigaChat", callback_data="GigaChat")
    await message.answer(
        "Выберите модель для ответа:",
        reply_markup=builder.as_markup(),
    )
    await state.set_state(ModelChoice.waiting_for_question)


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: types.Message, state: FSMContext):
    """
    Обработчик команд /start и /help.
    """
    await send_model_selection(message, state)


@dp.message(Command(commands=["change_model"]))
async def change_model(message: types.Message, state: FSMContext):
    """
    Обработчик команды /change_model.
    """
    await send_model_selection(message, state)


@dp.callback_query(lambda c: c.data in ["ChatGroq", "GigaChat"])
async def process_model_choice(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(model=callback.data)
    await callback.message.answer(f"Выбрана модель {callback.data}. Теперь отправьте свой вопрос:")
    await callback.answer()
    await state.set_state(ModelChoice.waiting_for_question)  # Устанавливаем состояние после выбора модели

@dp.message()
async def handle_question(message: types.Message, state: FSMContext):
    """
    Обработчик всех текстовых сообщений (кроме команд).
    """
    data = await state.get_data()
    model_choice = data.get("model")  # Получаем модель, не указывая дефолт
    if not model_choice:
        await message.answer("Пожалуйста, выберите модель с помощью команд /start, /help или /change_model")
        return
    user_question = message.text

    await message.answer("Обрабатываю ваш запрос...")
    answer = await get_answer(user_question, model_choice)
    await message.answer(answer)
    await state.set_state(None) # Сбрасываем состояние waiting_for_question



async def main():
    """
    Функция запуска бота.
    """
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())