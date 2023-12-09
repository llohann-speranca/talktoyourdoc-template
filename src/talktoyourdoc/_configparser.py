from pathlib import Path
from configparser import ConfigParser
CURRENT_DIR = Path(__file__).parent.resolve()
ROOT_DIR = Path(__file__).parents[2]
DATABASE_DIR = ROOT_DIR / 'database'
CONFIG_FILE = ROOT_DIR / 'config.ini'


