from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    FSUB = getenv("FSUB", "SDBotz")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO", "5023815012 6184402222 6387145248 1877279215 6067718572").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
