from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

from filters.chat_types import ChatTypeFilter
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

user_advert_router = Router()
user_advert_router.message.filter(ChatTypeFilter(['private']))

first_photo = LEXICON_PRICE['first_photo']
photo_podlojka = LEXICON_PRICE['photo_podlojka']
banner_top = LEXICON_PRICE['banner_top']
brendbox = LEXICON_PRICE['brendbox']
brendbox_heading = LEXICON_PRICE['brendbox_heading']
brendbox_heading_new = LEXICON_PRICE['brendbox_heading_new']
floating = LEXICON_PRICE['floating']
banner_horizontal = LEXICON_PRICE['banner_horizontal']
advertising_news = LEXICON_PRICE['advertising_news']
brendbox_premium = LEXICON_PRICE["brendbox_premium"]


# Список ID фотографий
photo_ids = [first_photo, photo_podlojka, banner_top, brendbox, brendbox_heading, brendbox_heading_new, floating, banner_horizontal, advertising_news,  brendbox_premium]

caption_dict = {
    first_photo: LEXICON_PRICE['first_photo_info'],
    photo_podlojka: LEXICON_PRICE['podlojka_info'],
    banner_top: LEXICON_PRICE['banner_top_info'],
    brendbox: LEXICON_PRICE['brendbox_info'],
    brendbox_heading: LEXICON_PRICE['brendbox_heading_info'],
    brendbox_heading_new: LEXICON_PRICE['brendbox_heading_info_new'],
    floating: LEXICON_PRICE['floating_info'],
    banner_horizontal: LEXICON_PRICE['banner_horizontal_info'],
    advertising_news: LEXICON_PRICE['advertising_news_info'],
    brendbox_premium: LEXICON_PRICE['brendbox_premium_info'],
}

current_photo_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'site_slivki_advertising')
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Следующее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_photo')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next)


# Обработчик инлайн кнопки "Предыдущее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_photo')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next)


################################# insta ################################

from aiogram import Router, F, types, Bot
from aiogram.types import Message, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexicon.lexicon import LEXICON_PRICE, LEXICON_btn_main_menu

router = Router()

insta1 = LEXICON_PRICE['insta1']
insta2 = LEXICON_PRICE['insta2']
insta3 = LEXICON_PRICE['insta3']
insta4 = LEXICON_PRICE['insta4']
insta5 = LEXICON_PRICE['insta5']


# Список ID фотографий
photo_ids = [insta1, insta2, insta3, insta4, insta5]

caption_dict = {
    insta1: LEXICON_PRICE['insta_info1'],
    insta2: LEXICON_PRICE['insta_info2'],
    insta3: LEXICON_PRICE['insta_info3'],
    insta4: LEXICON_PRICE['insta_info4'],
    insta5: LEXICON_PRICE['insta_info5'],
}

current_photo_index = 0

button_next = InlineKeyboardButton(
    text='ВПЕРЕД',
    callback_data='next_photo_insta')
button_prev = InlineKeyboardButton(
    text='НАЗАД',
    callback_data='prev_photo_insta')
# button_manager = InlineKeyboardButton(
#     text=LEXICON_btn_main_menu['manager'],
#     callback_data='manager')
button_back_to_preview_menu = InlineKeyboardButton(
    text='Назад в меню',
    callback_data='price_statistic')
keyboard_prev_next: list[list[InlineKeyboardButton]] = [
    [button_prev, button_next],
    [button_back_to_preview_menu]
]
markup_prev_next_insta = InlineKeyboardMarkup(inline_keyboard=keyboard_prev_next)


@user_advert_router.callback_query(F.data == 'instagram_sl')
# async def on_start(message: Message, bot: Bot):
async def on_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_ids[current_photo_index],
                         caption=caption_dict[photo_ids[current_photo_index]],
                         reply_markup=markup_prev_next_insta)


# Обработчик инлайн кнопки "Следующее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'next_photo_insta')
async def on_next_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index + 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_insta)


# Обработчик инлайн кнопки "Предыдущее фото"
@user_advert_router.callback_query(lambda callback_query: callback_query.data == 'prev_photo_insta')
async def on_prev_photo(callback: types.CallbackQuery, bot: Bot):
    global current_photo_index
    current_photo_index = (current_photo_index - 1) % len(photo_ids)
    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=InputMediaPhoto(
                                     media=photo_ids[current_photo_index],
                                     caption=caption_dict[photo_ids[current_photo_index]],
                                 ),
                                 reply_markup=markup_prev_next_insta)