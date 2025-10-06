from sqlalchemy import insert, update, delete, select

class UsersRepository():
    def __init__(self, engine, users_table):
        self.engine = engine
        self.users_table = users_table


    def insert_user(self, name, email):
        stmt = insert(self.users_table).values(name = name, email = email)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        
        return result
    
    def update_user_by_id(self, user_id, name, email):
        stmt = update(self.users_table).where(self.users_table.c.id == user_id).values(name=name, email=email)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)

        return result
    
    def delete_user_by_id(self, user_id):
        stmt = delete(self.users_table).where(self.users_table.c.id == user_id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        
        return result


    def get_all_users(self):
        stmt = select(self.users_table)
        with self.engine.connect() as conn:
            results = conn.execute(stmt).mappings().all()
        
        return results