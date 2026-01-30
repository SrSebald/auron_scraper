import sqlite3
from ajefech_client import filter_santiago_presencial
from datetime import date, datetime

DB_PATH = "data/ajefech.db"

def create_table():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS tournaments (
    id TEXT PRIMARY KEY, 
    title TEXT, 
    city TEXT, 
    address TEXT, 
    start_date DATE, 
    start_date_iso DATE,
    is_online INTEGER , 
    is_santiago INTEGER,  
    is_suspended INTEGER,
    scraped_at TIMESTAMP);
    """
    cursor.execute(create_table_query)
    conn.commit
    conn.close
    
    filter_santiago_presencial(list)

"""Esta función me supero ligeramente: repasar"""
def upsert_tournaments(tournaments: list[dict]) -> None:
    insert_query = """
    INSERT OR IGNORE INTO tournaments (
        id, title, city, address,
        start_date, start_date_iso,
        is_online, is_santiago, is_suspended,
        scraped_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    scraped_at = datetime.now().isoformat(timespec="seconds")

    rows = []
    for t in tournaments:
        # start_date_obj puede ser date o None
        start_date_obj = t.get("start_date_obj")
        start_date_iso = start_date_obj.isoformat() if start_date_obj is not None else None

        row = (
            t.get("id", ""),
            t.get("title", ""),
            t.get("city_clean", t.get("city", "")),
            t.get("address_clean", t.get("address", "")),
            t.get("start_date", ""),
            start_date_iso,
            int(bool(t.get("is_online"))),
            int(bool(t.get("is_santiago"))),
            int(bool(t.get("is_suspended"))),
            scraped_at,
        )
        rows.append(row)

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.executemany(insert_query, rows)
        conn.commit()
    finally:
        conn.close()
        
        

def pasar_a_csv ():
    return True  




def get_latest(n: int = 10):
    """
    Devuelve los próximos N torneos ordenados por start_date_iso (asc).
    (Puedes cambiar el WHERE si quieres solo Santiago presencial.)
    """
    query = """
    SELECT
        id, title, city, address,
        start_date, start_date_iso,
        is_online, is_santiago, is_suspended,
        scraped_at
    FROM tournaments
    WHERE start_date_iso IS NOT NULL
    ORDER BY start_date_iso ASC
    LIMIT ?;
    """

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(query, (n,))
        return cursor.fetchall()
    finally:
        conn.close()

