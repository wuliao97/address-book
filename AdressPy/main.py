# import click
import sys
from sql import get_conn, insert_or_update, create_table, get_one
from util.model import AddrStd


def main(db_url: str | None):
    conn = get_conn(db_url)
    create_table(conn)

    std_type = AddrStd(
        "Ennui",
        "8170-0000-111",
        "0000",
        "Chiyodaku",
        "Tokyo-to",
        "Japan",
        "1000 000",
    )
    insert_or_update(conn, std_type)

    result = get_one(conn, "Ennui")
    from pprint import pprint
    pprint(result)


if __name__ == "__main__":
    if "debugpy" in sys.modules:
        url = "db/address.db"
    else:
        url = None

    main(url)
