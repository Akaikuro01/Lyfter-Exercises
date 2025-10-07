from sqlalchemy import insert, update, delete, select, create_engine
from sqlalchemy.exc import IntegrityError
from db import db_context

class RoleRepository:
    def __init__(self, engine):
        self.engine = engine
        self.insert_default_roles()
    
    #Since this is an exercise with only 2 roles, I am hardcoding them and inserting them here. I made the name unique so when it comes and does the insert again, it just does nothing.
    def insert_default_roles(self):
        try:
            stmt = insert(db_context.roles_table).values([{"name": "admin"}, {"name": "user"}])
            with self.engine.begin() as conn:
                conn.execute(stmt)
        except IntegrityError:
            print("Default roles already inserted")


    # def get_roles(self):
    #     stmt = select(db_context.roles_table.c.name)
    #     with self.engine.connect() as conn:
    #         roles = conn.execute(stmt).scalars().all()
    #         if(len(roles)==0):
    #             return None
    #         else:
    #             return roles