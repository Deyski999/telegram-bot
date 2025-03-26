from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from db import users_collection

TOKEN = "7738161946:AAGUdgUDLFucQebMsCQih_7k47wz24fc4CY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Save user to MongoDB
    users_collection.update_one(
        {"_id": user.id},
        {"$set": {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        }},
        upsert=True
    )

    await update.message.reply_text("Hello! You’ve been saved to MongoDB 😎")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
