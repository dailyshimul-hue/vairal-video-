import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ══════════════════════════════════════════
#  এখানে আপনার নতুন BOT TOKEN বসান
BOT_TOKEN = "8835737635:AAEo-us5MJiP1ZUEUFvbp-CNNsFTBakuP3s"

#  আপনার Private Group ID
GROUP_ID = -1003978616422
# ══════════════════════════════════════════

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args  # start parameter (message ID)

    if args:
        # Website থেকে এসেছে - message ID দিয়ে ভিডিও forward করো
        try:
            msg_id = int(args[0])
            await context.bot.forward_message(
                chat_id=user.id,
                from_chat_id=GROUP_ID,
                message_id=msg_id
            )
        except Exception as e:
            await update.message.reply_text(
                "❌ ভিডিও পাঠাতে সমস্যা হয়েছে। একটু পরে চেষ্টা করুন।"
            )
            logging.error(f"Forward error: {e}")
    else:
        # সরাসরি বটে এসেছে
        await update.message.reply_text(
            f"👋 হ্যালো {user.first_name}!\n\n"
            "🎬 Vairal Video ওয়েবসাইট থেকে ডাউনলোড করুন:\n"
            "👉 আপনার সাইটের লিংক দিন এখানে\n\n"
            "📢 আমাদের চ্যানেল: https://t.me/+mnRNVatANUk5MTZl"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot চালু হয়েছে...")
    app.run_polling()

if __name__ == "__main__":
    main()
