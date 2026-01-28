import sqlite3
from ajefech_client import filter_santiago_presencial
from datetime import date, datetime

def create_table():
    DB_PATH = "data/ajefech.db"

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS tournaments (
    id PRIMARY KEY o UNIQUE, 
    title TEXT, 
    city TEXT, 
    address TEXT, 
    start_date DATE, 
    start_date_iso DATE,
    is_online INTEGER , 
    is_santiago INTEGER,  
    is_suspended INTEGER,
    scraped_at TIMESTAMP
    """
    cursor.execute(create_table_query)
    conn.commit
    conn.close
    

def upsert_tournaments(tournaments: list[dict]):
    DB_PATH = "data/ajefech.db"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for t in filtered_sorted:

        insert_query = """
        INSERT OR IGNORE INTO tournaments (id, tittle, city, address, 
        start_date, start_date_iso, is_online, is_santiago, is_suspended, scraped_at) 
        VALUES ()
        """
        int(t["is_santiago"]),
        int(t["is_suspended"]),
        int(t["is_online"]),
        t["start_date_obj"].isoformat()

    filtered_sorted = filter_santiago_presencial()

def get_lastet (n = 10): 
    return True

