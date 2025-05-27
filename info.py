import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '27081782'))
API_HASH = environ.get('API_HASH', 'cf31454dd0855b182ce75f2903fefad4')
BOT_TOKEN = environ.get('BOT_TOKEN', "7534842089:AAEuRFKvZA1MtZH_q5J8IadlWIAiZl1Dk1E")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002573308648'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7834603779 6225794321').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vijay887108:bTTaSmAQKfd6Epnk@cluster0.c8lvuda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjautobot")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', false)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
