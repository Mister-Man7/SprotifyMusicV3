import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999999999))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1854441420))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Mister-Man7/SprotifyMusicV3",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/estropolis")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/datarantinggi")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 99))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 10737418240))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 10737418240))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @SessionMotherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#  ____    _    _  ___  ___   _   __  __ _   _ ____ ___ ____   ____   ___ _____ 
# / ___|  / \  | |/ / |/ / | | | |  \/  | | | / ___|_ _/ ___| | __ ) / _ \_   _|
# \___ \ / _ \ | ' /| ' /| | | | | |\/| | | | \___ \| | |     |  _ \| | | || |  
#  ___) / ___ \| . \| . \| |_| | | |  | | |_| |___) | | |___  | |_) | |_| || |  
# |____/_/   \_\_|\_\_|\_\\___/  |_|  |_|\___/|____/___\____| |____/ \___/ |_|  
                                                                               



BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/afe0bf9e6b4fede3afc0e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/8f6de108a54be6506b693.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/94074fd8f348807833802.jpg"
STATS_IMG_URL = "https://graph.org/file/c9266ed41c1a9b8121185.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/f626eb194b025672eea28.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f6e977e0046a5b8d17904.jpg"
STREAM_IMG_URL = "https://graph.org/file/7247dcb0ae280ba3b8492.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/199a1bd803d3e8c8d0e43.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/d902a638d7bcb6653d36f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/dc9eb455f86f845f400f8.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/aacfa8762c016077b7ee9.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/480dbdc265670e833d763.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

    
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)





