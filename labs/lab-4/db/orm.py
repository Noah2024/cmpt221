"""orm.py: sqlalchemy orm used to manage the Professors table"""
from db.server import get_session
from db.schema import Professor

"""Lab 4 - Part 2:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table
"""

def get_all_professors():
    """Select all records from the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # get all entries in the Professors table
        professors = session.query(Professor).all()
        return professors
    
    finally:
        session.close()

def insert_professors():
    """Insert 3 records into the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: create three professor objects
        # TODO: use the sqlalchemy orm to insert the new records as a list of professor objects
        # "save" the changes
        billy = Professor(ProfessorFirstName = 'Billy', ProfessorLastName = 'Jean', ProfessorEmailAddress = 'BillyJean@gmail.com')
        Bob = Professor(ProfessorFirstName = 'Bob', ProfessorLastName = 'Joe', ProfessorEmailAddress = 'BobJoe@gmail.com')
        Jill = Professor(ProfessorFirstName = 'Jill', ProfessorLastName = 'Stein', ProfessorEmailAddress = 'JillStein@gmail.com')
        session.add_all([billy, Bob, Jill])
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting professors:", e)

    finally:
        session.close()

def update_professor():
    """Update one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    from sqlalchemy import select
    try:
        stmt = select(Professor).where(Professor.ProfessorFirstName == 'Jill')
        jill = session.scalars(stmt).first()
        jill.Email = 'JillBill@Gmail.com'
        # TODO: get professor to be updated (would ideally be a parameter)
        # TODO: use the sqlalchemy orm to update 1 record
        # "save" the changes
        session.commit()
    
    except Exception as e:
        print("Error updating professor:", e)
        session.rollback()
    finally:
        session.close()

def delete_professor():
    """Delete one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    from sqlalchemy import select
    try:
        # TODO: get professor to be deleted (would ideally be a parameter)
        # TODO: use the sqlalchemy orm to delete 1 record
        # "save" the changes
        stmt = select(Professor).where(Professor.ProfessorFirstName == 'Bob')
        bob = session.scalars(stmt).first()
        session.delete(bob)
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)

    finally:
        session.close()

