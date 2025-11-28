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

    def get_products_by_id(self, _id):
        stmt = select(db_context.product_table).where(db_context.product_table.c.id == _id)
        with self.engine.connect() as conn:
            products = conn.execute(stmt).mappings().one_or_none()

            if(products == None):
                return None
            else:
                return dict(products)
            
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