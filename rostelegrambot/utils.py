from telegram import Update
from telegram.ext import CallbackContext

from ros import Ros


def get_ros(update: Update, context: CallbackContext):
    assert context.user_data
    if "ros" not in context.user_data:
        url: str = context.user_data["server"]
        server: dict = context.user_data["server_data"]
        ros = Ros(url)
