import sqlite3
from pathlib import Path


def load_schema(path: Path) -> str:
    """Load an sqlite3 schema from a specified path

    :param path: The path to the schema
    :type path: Path
    :return: The schema as a string
    :rtype: str
    """
    with path.open() as file:
        return file.read()


def init_db(db: Path, schema: Path) -> None:
    """Initialize a specified database with a schema

    :param db: The path to the database
    :type db: Path
    :param schema: The path to the schema
    :type schema: Path
    """
    conn = sqlite3.connect(db)

    _schema = load_schema(schema)
    conn.executescript(_schema)

    conn.commit()
    conn.close()
