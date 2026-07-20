import os
from flask import Flask, request, jsonify
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(TOKEN)
app = Flask(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="مرحبا! البوت راه خدام ✅")

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def index():
    return "Bot is alive"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
