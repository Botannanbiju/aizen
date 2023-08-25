from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://admin:admin@cluster0.iteow9t.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "c869e87de280d98b363fced8e492ab40"]
        API_ID = [int, 13487236]
        BOT_TOKEN = [str, "6656070271:AAFn5vULYHh_9L5-fbDYKCCT5MBz3DmYLtk"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[]]
        OWNER_ID = [int, 5491384523]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/OngoingStartAnimeFF"]
        FORCEJOIN_ID = [int, -1001974889758]

        TRACE_CHANNEL = [int, -1001929866719]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
