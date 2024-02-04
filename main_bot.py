import telebot
from telebot import types
from telebot.types import WebAppInfo
import info
import threading

bot = telebot.TeleBot(
    info.BOT_TOKEN
)


markup_reply = types.ReplyKeyboardMarkup()

button_1_reply = types.KeyboardButton(
    "Open google.com", web_app=WebAppInfo(url="https://google.com")
)

markup_reply.add(button_1_reply)

lock = threading.Lock()

@bot.message_handler(commands=["start"])
def start(message):
    with lock:
        bot.send_message(
            message.chat.id,
            "Hello",
            reply_markup=markup_reply
        )

if __name__ == "__main__":
    bot.infinity_polling()
