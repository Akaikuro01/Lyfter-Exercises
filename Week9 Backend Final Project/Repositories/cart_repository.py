from sqlalchemy import insert, update, delete, select, create_engine, and_, func
from db import db_context

class CartRepository:
    def __init__(self, engine):
        self.engine = engine
        
    def insert_shopping_cart(self, date_created, user_id):
        stmt = insert(db_context.shopping_cart_table).returning(db_context.shopping_cart_table.c.id).values(date_created=date_created, user_id=user_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return int(result.all()[0][0])
    
    def insert_cart_items(self, items):
        stmt = insert(db_context.cart_items_table).returning(db_context.cart_items_table.c.id).values(items)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]
    
    # def get_total_invoice_by_id(self, invoice_id):
    #     stmt = select(
    #         func.sum(db_context.invoice_lines_table.c.subtotal).label("total")
    #     ).where(db_context.invoice_lines_table.c.invoice_id == invoice_id)

    #     with self.engine.connect() as conn:
    #         total = conn.execute(stmt).scalar_one()

    #     return float(total)

    def update_cart_items(self, user_id, product_id, quantity):
        sc = db_context.shopping_cart_table
        ci = db_context.cart_items_table
        stmt = (
            update(ci)
            .values(quantity=quantity)
            .where(
                ci.c.product_id == product_id,
                ci.c.cart_id == sc.c.id,
                sc.c.user_id == user_id,
            )
        )
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result


    def get_cart_info_by_user(self, user_id):
        sc = db_context.shopping_cart_table
        ci = db_context.cart_items_table
        p  = db_context.product_table
        u  = db_context.user_table

        stmt = select(
            sc.c.id.label("cart_id"),
            u.c.username,
            p.c.id.label("product_id"),
            p.c.name.label("product_name"),
            p.c.unit_price,
            ci.c.quantity).select_from(            
                sc.join(ci, sc.c.id == ci.c.cart_id)
                .join(p, ci.c.product_id == p.c.id)
                .join(u, sc.c.user_id == u.c.id)).where(sc.c.user_id == user_id).order_by(sc.c.id)
        
        with self.engine.connect() as conn:
            shopping_cart = conn.execute(stmt).mappings().all()

            if(len(shopping_cart)==0):
                return None
            else:
                return [dict(i) for i in shopping_cart]
            
    def delete_cart_by_user_id(self, user_id):
        stmt = (delete(db_context.shopping_cart_table)
                .where(db_context.shopping_cart_table.c.user_id == user_id))
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result
    
    def delete_cart_by_id(self, cart_id):
        stmt = (delete(db_context.shopping_cart_table)
                .where(db_context.shopping_cart_table.c.id == cart_id))
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result