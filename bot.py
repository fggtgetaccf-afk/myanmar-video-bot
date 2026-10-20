import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN မသတ်မှတ်ရသေးပါ")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "မင်္ဂလာပါ။ မြန်မာအသံပြန်ဆို Video Bot မှ ကြိုဆိုပါတယ်။ 🎬\n"
        "Video ပို့ပေးပါ။ လက်ရှိမှာ Bot စမ်းသပ်ဆဲဖြစ်ပါတယ်။"
    )

@bot.message_handler(content_types=["video"])
def receive_video(message):
    bot.reply_to(
        message,
        "✅ Video လက်ခံရရှိပါပြီ။\n"
        "မြန်မာအသံပြန်ဆိုစနစ်ကို ဆက်လက်တည်ဆောက်နေပါတယ်။"
    )

bot.infinity_polling(skip_pending=True)
