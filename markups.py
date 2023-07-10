from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('главное меню')

# -- main menu ---
btnRandom = KeyboardButton('Рандомное число')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)

# -- other menu ---
btnInfo = KeyboardButton('Info')
btnMoney = KeyboardButton('курсы валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)