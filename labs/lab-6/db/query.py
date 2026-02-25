"""query.py: leverages SQLAlchemy to create generic queries for interacting with the postgres DB"""
from db.server import get_session

def get_all(table) -> list:
    """Select all records from a DB table using SQLAlchemy ORM."""
    session = get_session()
    try:
        records = session.query(table).all()
        return records
    finally:
        session.close()

def insert(record):
    """Insert a new record into the database."""
    session = get_session()
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Error inserting record:", e)
    finally:
        session.close()
