import telebot
from telebot import types
from telebot.types import WebAppInfo
import info

bot = telebot.TeleBot(
    info.BOT_TOKEN
)


markup_reply = types.ReplyKeyboardMarkup()

button_1_reply = types.KeyboardButton(
    "Open google.com", web_app=WebAppInfo(url="https://google.com")
)

markup_reply.add(button_1_reply)


@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id,
        "Hello",
        reply_markup=markup_reply
    )


bot.infinity_polling()
