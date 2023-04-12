import sqlite3
from datetime import datetime

DB_NAME = "one_word_story.db"
SCHEMA_NAME = "schema.sql"


def set_channel(conn: sqlite3.Connection, channel_id: int, guild_id: int) -> None:
    """Set the channel to be used with one work story

    :param conn: The database connection
    :type conn: sqlite3.Connection
    :param channel_id: The channel id
    :type channel_id: int
    :param guild_id: The guild id
    :type guild_id: int
    """
    query = """
    INSERT OR REPLACE INTO channels (channel_id, guild_id, date_updated)
    VALUES (?, ?, ?)
    """
    date_updated = datetime.utcnow().isoformat()

    cursor = conn.cursor()
    cursor.execute(query, (channel_id, guild_id, date_updated))
    conn.commit()
