import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

CONTACTS_DATABASE = os.getenv("CONTACTS_DATABASE") or 'contacts_database.db'
CONTACTS_DATABASE_PATH = os.path.join(dirname, 'data', CONTACTS_DATABASE)

DATABASE_TABLES = os.getenv('DATABASE_TABLES') or 'database_tables.csv'
DATABASE_TABLES_PATH = os.path.join(dirname, 'data', DATABASE_TABLES)
