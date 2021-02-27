import logging
from aiogram import Bot, Dispatcher, executor, types
from parse.Parse import Voronezh1,Pridacha


API_TOKEN = int

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


departure_voronezh1_btn = types.inline_keyboard.InlineKeyboardButton(text='Отправление', callback_data='voronezh1_departure') 
arrival_voronezh1_btn = types.inline_keyboard.InlineKeyboardButton(text='Прибытие', callback_data='voronezh1_arrival') 
schedule_voronezh1_btn = types.inline_keyboard.InlineKeyboardButton(text='Всё расписание', callback_data='voronezh1_schedule') 

departure_pridacha_btn = types.inline_keyboard.InlineKeyboardButton(text='Отправление', callback_data='pridacha_departure') 
arrival_pridacha_btn = types.inline_keyboard.InlineKeyboardButton(text='Прибытие', callback_data='pridacha_arrival') 
schedule_pridacha_btn = types.inline_keyboard.InlineKeyboardButton(text='Всё расписание', callback_data='pridacha_schedule') 

menu = types.inline_keyboard.InlineKeyboardButton(text="Меню", callback_data=f"menu")




@dp.message_handler(commands=['start'])
async def strat_message(message: types.Message,mode='text'):
    start_text = 'Выберите интересующую вас станцию:'
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2)

    voronezh1_btn = types.inline_keyboard.InlineKeyboardButton(text='ВОРОНЕЖ 1 🚆 ', callback_data='voronezh1' )
    pridacha_btn = types.inline_keyboard.InlineKeyboardButton(text='ПРИДАЧА 🚆', callback_data='pridacha' )
    markup.row(voronezh1_btn, pridacha_btn)
    if mode == 'text': 
        return await message.answer(f'*{start_text}*', parse_mode='Markdown', reply_markup=markup)
    elif mode == 'edit':
        return await bot.edit_message_text(text=f'*{start_text}*',reply_markup=markup, parse_mode="MARKDOWN", message_id=message.message_id, chat_id=message.chat.id)


@dp.callback_query_handler(text='voronezh1')
async def voronezh1(call: types.CallbackQuery):
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(departure_voronezh1_btn,arrival_voronezh1_btn,schedule_voronezh1_btn,menu)
    await call.bot.edit_message_text(f'*Выберите действие:*', parse_mode='Markdown', reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)
    

@dp.callback_query_handler(text='pridacha')
async def pridacha(call: types.CallbackQuery):
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(departure_pridacha_btn,arrival_pridacha_btn,schedule_pridacha_btn,menu)
    await call.bot.edit_message_text(f'*Выберите действие:*', parse_mode='Markdown', reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)



@dp.callback_query_handler(text='voronezh1_departure')
async def get_Voronezh1_departure(call: types.CallbackQuery):
    text_departure=Voronezh1.Voronezh1_departure()
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
    await call.bot.edit_message_text(f'*Отправление:\n\n{text_departure}*', parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)

@dp.callback_query_handler(text='voronezh1_arrival')
async def get_Voronezh1_arrival(call: types.CallbackQuery):
    text_arrival=Voronezh1.Voronezh1_arrival()
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
    await call.bot.edit_message_text(f'*Прибытие:\n\n{text_arrival}*', parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)

@dp.callback_query_handler(text='voronezh1_schedule')
async def get_schedule_voronezh1(call: types.CallbackQuery):
    content=Voronezh1.Voronezh1_get_content()
    if len(content) > 4096:
        for x in range(0, len(content), 4096):
            res = content[x:x+4096]
            markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
            await call.bot.edit_message_text(f"*{res}*", parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)
        
    else:
        markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
        await call.bot.edit_message_text(f"*{content}*", parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)



@dp.callback_query_handler(text='pridacha_departure')
async def get_Pridacha_departure(call: types.CallbackQuery):
    text_departure=Pridacha.Pridacha_departure()
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
    await call.bot.edit_message_text(f'*Отправление:\n\n{text_departure}*', parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)

@dp.callback_query_handler(text='pridacha_arrival')
async def get_Pridacha_arrival(call: types.CallbackQuery):
    text_arrival=Pridacha.Pridacha_arrival()
    markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
    await call.bot.edit_message_text(f'*Прибытие:\n\n{text_arrival}*', parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)

@dp.callback_query_handler(text='pridacha_schedule')
async def get_schedule_pridacha(call: types.CallbackQuery):
    content = Pridacha.Pridacha_get_content()
    if len(content) > 4096:
        for x in range(0, len(content), 4096):
            res = content[x:x+4096]
            markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
            await call.bot.edit_message_text(f"*{res}*", parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)
        
    else:
        markup = types.inline_keyboard.InlineKeyboardMarkup(row_width=2).add(menu)
        await call.bot.edit_message_text(f"*{content}*", parse_mode='Markdown',reply_markup=markup, message_id=call.message.message_id,chat_id=call.message.chat.id)


@dp.callback_query_handler(text_contains="menu")
async def get_menu(call: types.CallbackQuery):
    await strat_message(call.message, mode='edit')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
