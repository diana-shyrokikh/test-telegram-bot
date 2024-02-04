import telebot
from telebot import types
from telebot.types import WebAppInfo
from aiohttp import web
import info
# import threading


WEBHOOK_HOST = "https://test-tekegram-bot.onrender.com"
WEBHOOK_PATH = f"/webhook/{info.BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBAPP_HOST = "0.0.0.0"
bot = telebot.TeleBot(
    info.BOT_TOKEN,
)
app = web.Application()


markup_reply = types.ReplyKeyboardMarkup()

button_1_reply = types.KeyboardButton(
    "Open google.com", web_app=WebAppInfo(url="https://google.com")
)

markup_reply.add(button_1_reply)

# lock = threading.Lock()

@bot.message_handler(commands=["start"])
def start(message):
    # with lock:
    bot.send_message(
        message.chat.id,
        "Hello",
        reply_markup=markup_reply
    )


bot.remove_webhook()
bot.set_webhook(
    WEBHOOK_URL,
    drop_pending_updates=False
)

web.run_app(
    app,
    host="test-tekegram-bot.onrender.com",
    port=8443,
)
