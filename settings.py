"""
Settings module.

Contains bot settings.
"""

from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

TELEGRAM_TOKEN = environ.get('TELEGRAM_TOKEN')
