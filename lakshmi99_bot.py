import telebot
import os
from telebot import types

BOT_TOKEN = os.environ["8066606951:AAG_bOJO-pSnPirxD0MD0yqWso14oX5LNrE"]
UPI_ID = os.environ["ravnasur@kotak"]
GROUP_LINK = os.environ["https://t.me/+i_-b1hqk3UI0YjE1"]

bot = telebot.TeleBot("8066606951:AAG_bOJO-pSnPirxD0MD0yqWso14oX5LNrE")

user_data = {}
ticket_counter = 1

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🙏 Welcome to Lakshmi99 Lottery!\nType /join to start.")

@bot.message_handler(commands=['join'])
def send_payment_info(message):
    caption = f"🎟 Entry Fee: ₹99\n\nSend UPI to: `{UPI_ID}`\nThen type /pay after payment."
    with open("assets/qr.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=caption, parse_mode="Markdown")

@bot.message_handler(commands=['pay'])
def request_screenshot(message):
    bot.reply_to(message, "📸 Please send your payment screenshot now.")

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    global ticket_counter
    uid = message.from_user.id
    if uid not in user_data:
        ticket = str(ticket_counter).zfill(4)
        ticket_counter += 1
        user_data[uid] = {"ticket": ticket, "username": message.from_user.username}
        bot.reply_to(message, f"✅ Payment received!\n🎟 Your Ticket No: {ticket}\n🔗 Join our group: {GROUP_LINK}")
    else:
        bot.reply_to(message, "✅ You already have a ticket.")

@bot.message_handler(commands=['myticket'])
def show_ticket(message):
    uid = message.from_user.id
    if uid in user_data:
        bot.reply_to(message, f"🎟 Your Ticket No: {user_data[uid]['ticket']}")
    else:
        bot.reply_to(message, "❌ You haven't paid yet.")

bot.polling()
