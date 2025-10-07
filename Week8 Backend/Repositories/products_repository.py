from sqlalchemy import insert, update, delete, select, create_engine
from db import db_context

class ProductRepository:
    def __init__(self, engine):
        self.engine = engine
        
    def insert_product(self, name, unit_price, entry_date, stock_qty):
        stmt = insert(db_context.product_table).returning(db_context.product_table.c.id).values(name=name, unit_price=unit_price, entry_date=entry_date, stock_qty=stock_qty)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


    def get_products(self, page, size, _id = None):
        if _id is None:
            stmt = select(db_context.product_table).order_by(db_context.product_table.c.id).offset((page - 1) * size).limit(size)
        else:
            stmt = select(db_context.product_table).where(db_context.product_table.c.id == _id)
        with self.engine.connect() as conn:
            products = conn.execute(stmt).mappings().all()

            if(products == None):
                return None
            else:
                #Since Date is not JSON serializable, I am creating a new list of dicts where I go through the results and cast the date to a JSON serializable value
                end_results = []
                for product in products:
                    results = dict(product)
                    results["entry_date"] = results["entry_date"].isoformat()
                    end_results.append(results)
                
                print(f"Products format: {end_results}")
                return end_results
            
    def update_products_by_id(self, _id, name, unit_price, entry_date, stock_qty):
        stmt = update(db_context.product_table).where(db_context.product_table.c.id == _id).values(name=name, unit_price=unit_price, entry_date=entry_date, stock_qty=stock_qty)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result
    
    def reduce_stock_product(self, product_id, quantity):
        stmt = update(db_context.product_table).where(db_context.product_table.c.id == product_id).values(stock_qty=db_context.product_table.c.stock_qty - quantity)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result
    
    def update_product_stock_by_id(self, _id, stock_qty):
        stmt = update(db_context.product_table).where(db_context.product_table.c.id == _id).values(stock_qty=stock_qty)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result
    
    def delete_products_by_id(self, _id):
        stmt = delete(db_context.product_table).where(db_context.product_table.c.id == _id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result