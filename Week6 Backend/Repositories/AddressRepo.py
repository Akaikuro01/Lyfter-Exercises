from sqlalchemy import insert, update, delete, select

class AddressRepository():
    def __init__(self, engine, address_table):
        self.engine = engine
        self.address_table = address_table


    def insert_address(self, address, user_id):
        stmt = insert(self.address_table).values(address = address, user_id = user_id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        
        return result
    
    def update_address_by_id(self, address_id, address, user_id):
        stmt = update(self.address_table).where(self.address_table.c.id == address_id).values(address=address, user_id=user_id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)

        return result
    
    def delete_address_by_id(self, address_id):
        stmt = delete(self.address_table).where(self.address_table.c.id == address_id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        
        return result
    
    def get_all_addresses(self):
        stmt = select(self.address_table)
        with self.engine.connect() as conn:
            results = conn.execute(stmt).mappings().all()
        
        return results
    