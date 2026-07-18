import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. جيب التوكن من Environment Variables تاع Render
TOKEN = os.environ.get("BOT_TOKEN")

# 2. انشئ التطبيق تاع تيليغرام
application = ApplicationBuilder().token(TOKEN).build()

# 3. انشئ سيرفر Flask تاع Render
app = Flask(name)

# 4. الكوموند /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا! البوت راه خدام ✅")

application.add_handler(CommandHandler("start", start))

# 5. الرابط اللي تيليغرام يبعث فيه الرسائل
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok"

# 6. الصفحة الرئيسية باش Render مايطفيش
@app.route("/")
def home():
    return "Bot is alive"

# 7. تشغيل السيرفر
if name == "main":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
