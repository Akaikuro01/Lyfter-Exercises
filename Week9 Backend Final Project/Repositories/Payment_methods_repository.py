from sqlalchemy import insert, update, delete, select, create_engine
from db import db_context

class PaymentMethodsRepository:
    def __init__(self, engine):
        self.engine = engine
        
    def insert_payment_method(self, user_id, brand, last4, exp_month, exp_year):
        stmt = insert(db_context.payment_methods_table).returning(db_context.payment_methods_table.c.id).values(user_id=user_id, brand=brand, last4=last4, exp_month=exp_month, exp_year=exp_year)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


    def get_payment_methods_by_user_id(self, user_id):
        stmt = select(db_context.payment_methods_table).where(db_context.payment_methods_table.c.id == user_id)
        with self.engine.connect() as conn:
            pm = conn.execute(stmt).mappings().one_or_none()

            if(pm == None):
                return None
            else:
                return dict(pm)

    def update_payment_methods_by_id(self, _id, user_id, brand, last4, exp_month, exp_year):
        stmt = (update(db_context.payment_methods_table)
                .where(db_context.payment_methods_table.c.id == _id)
                .values(user_id=user_id, brand=brand, last4=last4, exp_month=exp_month, exp_year=exp_year))
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result
        
    def delete_payment_methods_by_id(self, _id):
        stmt = delete(db_context.payment_methods_table).where(db_context.payment_methods_table.c.id == _id)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result