from telegram import Update
from telegram.ext import CallbackContext
from ros import Ros

def ping_command(update: Update, context: CallbackContext):
    if len(update.effective_message.text) == 5:
        update.effective_message.reply_text("Usage /ping address")
    ros: Ros = context.bot_data["ros"]
