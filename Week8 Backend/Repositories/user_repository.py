from sqlalchemy import insert, update, delete, select, create_engine
from db import db_context

class UserRepository:
    def __init__(self, engine):
        self.engine = engine
        
    def insert_user(self, username, password, role_id):
        stmt = insert(db_context.user_table).returning(db_context.user_table.c.id).values(username=username, password=password, role_id=role_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, username, password):
        stmt = select(db_context.user_table).where(db_context.user_table.c.username == username).where(db_context.user_table.c.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if(len(users)==0):
                return None
            else:
                return users[0]

    def get_user_by_id(self, id):
        stmt = select(db_context.user_table).where(db_context.user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]