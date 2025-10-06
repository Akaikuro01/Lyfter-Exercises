from sqlalchemy import insert, update, delete, select


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