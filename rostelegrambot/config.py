import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
IS_DEBUG = os.environ.get("IS_DEBUG", "N").lower() in ("true", "yes", "y")
ADMIN_CHAT_ID = os.environ.get("DEVELOPER_CHAT_ID", "")
