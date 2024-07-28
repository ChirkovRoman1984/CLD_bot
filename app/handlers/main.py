from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageCantBeDeleted

from app.handlers.bonus import med
from app.handlers.messages import cfg


async def cmd_start(message: types.Message):
    try:
        await message.delete()
    except MessageCantBeDeleted:
        pass
    await answer(message, 'start')


async def cmd_help(message: types.Message):
    try:
        await message.delete()
    except MessageCantBeDeleted:
        pass
    await answer(message, 'help')


async def cmd_dict(message: types.Message):
    try:
        await message.delete()
    except MessageCantBeDeleted:
        pass
    await answer(message, 'dictionary')


async def cmd_bonus(message: types.Message):
    try:
        await message.delete()
    except MessageCantBeDeleted:
        pass
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Назад", callback_data='start'),
        types.InlineKeyboardButton("Бонус", callback_data='bonus')
    )
    await message.answer(med.prikol, parse_mode="HTML", reply_markup=markup)


async def answer(message: types.Message, key: str) -> None:
    text, markup, img = cfg.get_all(key)
    if img:
        caption = cfg.get_caption(key)
        if caption:
            text = caption + '\n\n' + text
        await message.answer_photo(photo=img, caption=text, parse_mode="HTML", reply_markup=markup)
    else:
        await message.answer(text, parse_mode="HTML", reply_markup=markup)


async def text_handler(message: types.Message):
    await answer(message, 'text_handler')


async def callback_inline(call: types.CallbackQuery):
    try:
        await call.message.delete()
    except MessageCantBeDeleted:
        pass

    await answer(call.message, call.data)


async def callback_inline_bonus(call: types.CallbackQuery):
    await cmd_bonus(call.message)


def register_all_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=["start"], chat_type='private')
    dp.register_message_handler(cmd_help, commands=["help"], chat_type='private')
    dp.register_message_handler(cmd_dict, commands=["dict"], chat_type='private')
    dp.register_message_handler(cmd_bonus, commands=["bonus"], chat_type='private')
    dp.register_message_handler(text_handler, chat_type='private')
    dp.register_callback_query_handler(callback_inline_bonus, Text(startswith=['bonus']))
    dp.register_callback_query_handler(callback_inline)
