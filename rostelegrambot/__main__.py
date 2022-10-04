import logging
from telegram.ext import Updater

from .config import BOT_TOKEN, IS_DEBUG


def set_logging(debug: bool = IS_DEBUG):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.WARNING,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger("telegram.bot").setLevel(logging.WARNING)
    logging.getLogger("telegram.vendor.ptb_urllib3.urllib3.connectionpool").setLevel(
        logging.WARNING
    )


def main():
    set_logging()
    updater = Updater(token=BOT_TOKEN)


if __name__ == "__main__":
    main()
