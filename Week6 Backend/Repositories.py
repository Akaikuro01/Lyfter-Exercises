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
    

class VehicleRepository():
    def __init__(self, engine, vehicle_table):
        self.engine = engine
        self.vehicle_table = vehicle_table


    def insert_vehicle(self, brand, model, user_id=None):
        if user_id is not None:
            stmt = insert(self.vehicle_table).values(brand = brand, model = model, user_id = user_id) 
        else:  
            stmt = insert(self.vehicle_table).values(brand = brand, model = model)                     

        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        
        return result
    
    def update_vehicle_by_id(self, vehicle_id, brand, model, user_id):
        stmt = update(self.vehicle_table).where(self.vehicle_table.c.id == vehicle_id).values(brand=brand, model=model, user_id=user_id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)

        return result
    
    def delete_vehicle_by_id(self, vehicle_id):
        stmt = delete(self.vehicle_table).where(self.vehicle_table.c.id == vehicle_id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        
        return result
    
    def get_all_vehicles(self):
        stmt = select(self.vehicle_table)
        with self.engine.connect() as conn:
            results = conn.execute(stmt).mappings().all()
        
        return results