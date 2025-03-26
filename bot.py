import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from db import users_collection

TOKEN = os.environ["TELEGRAM_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user

        users_collection.update_one(
            {"_id": user.id},
            {"$set": {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
            }},
            upsert=True
        )

        await update.message.reply_text("✅ You’ve been saved to MongoDB!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()