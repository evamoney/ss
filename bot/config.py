import os


class Config:

    API_ID = int(os.environ.get("API_ID", '13126185'))
    API_HASH = os.environ.get("API_HASH", '945d34fcce68f4bffc600fa702ca1506')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '5723345756:AAGEM_NH8S9IzfL7VT7bzEjVn-_pBQQU47M')
    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1001899072167'))
    DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://kwicbot:kwicbot@cluster0.ecyjnnk.mongodb.net/?retryWrites=true&w=majority')
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "942099709").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "0.0.0.0")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
