from django.conf import settings
import telebot
def send_message(message):
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)