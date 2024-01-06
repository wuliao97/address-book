import sqlite3 as sqlite
from util.model import AddrStd
from typing import Optional


def create_table(pool: sqlite.Connection):
    pool.execute("""CREATE TABLE IF NOT EXISTS address(
        name TEXT PRIMARY KEY,
        phone_number TEXT NOT NULL,
        address_line TEXT NOT NULL,
        city TEXT NOT NULL,
        region TEXT NOT NULL,
        country TEXT NOT NULL,
        post_code TEXT NOT NULL
    )
    """)


def get_conn(url: Optional[str]) -> sqlite.Connection:
    if not url:
        url = ":memory:"
    conn = sqlite.connect(url)
    return conn


def insert_or_update(pool: sqlite.Connection, data: AddrStd):
    cur = pool.cursor()
    cur.execute(
        """INSERT INTO address values (?, ?, ?, ?, ?, ?, ?) 
        ON CONFLICT (name) DO UPDATE SET
        phone_number = ?, address_line = ?, city = ?, region = ?, country = ?, post_code = ?;
        """,
        (
            data.name, data.phone_number, data.address_line, data.city, data.region, data.country, data.post_code,
            data.phone_number, data.address_line, data.city, data.region, data.country, data.post_code
         )
    )
    # cur.execute("""CREATE INDEX name_index ON address(name)""")
    pool.commit()


def get_one(pool: sqlite.Connection, key: str):
    data = pool.execute("SELECT * FROM address WHERE name = ?", (key, ))
    return data.fetchone()
