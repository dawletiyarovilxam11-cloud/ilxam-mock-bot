import telebot
from telebot import types

TOKEN = "8404481882:AAGDkpiUBTIaMoe60kWDSc8nU7NBzeC5VwI"
ADMIN_ID = 6278514680  # <-- bu yerga o'zingizning Telegram ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("PART 1.1", "PART 1.2")
    markup.add("PART 2", "PART 3")
    bot.send_message(message.chat.id,
                     "Welcome to Ilxam Mock Speaking Test 🎤\n\nSelect the part and send your audio.",
                     reply_markup=markup)

@bot.message_handler(content_types=['voice','audio'])
def handle_audio(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ Audio received successfully. Wait for your band score.")

@bot.message_handler(func=lambda message: True)
def handle_part(message):
    bot.send_message(message.chat.id, f"You selected {message.text}. Now send your audio (1-2 minutes).")

bot.infinity_polling()
