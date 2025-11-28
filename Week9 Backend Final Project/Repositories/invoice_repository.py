from sqlalchemy import insert, update, delete, select, create_engine, and_, func
from db import db_context

class InvoiceRepository:
    def __init__(self, engine):
        self.engine = engine
        
    def insert_invoice_headers(self, sale_date, total_amount, invoice_address, payment_method, user_id):
        stmt = insert(db_context.invoice_header_table).returning(db_context.invoice_header_table.c.id).values(sale_date=sale_date, total_amount=total_amount, invoice_address=invoice_address, payment_method=payment_method, user_id=user_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return int(result.all()[0][0])
    
    def insert_invoice_lines(self, lines):
        stmt = insert(db_context.invoice_lines_table).returning(db_context.invoice_lines_table.c.id).values(lines)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]
    
    def get_total_invoice_by_id(self, invoice_id):
        stmt = select(
            func.sum(db_context.invoice_lines_table.c.subtotal).label("total")
        ).where(db_context.invoice_lines_table.c.invoice_id == invoice_id)

        with self.engine.connect() as conn:
            total = conn.execute(stmt).scalar_one()

        return float(total)

    def update_total_amount_invoice_headers(self, total, invoice_id):
        stmt = update(db_context.invoice_header_table).where(db_context.invoice_header_table.c.id == invoice_id).values(total_amount=total)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        return result

    def get_invoice_info_by_user(self, user_id, page, size):
        ih = db_context.invoice_header_table
        il = db_context.invoice_lines_table
        p  = db_context.product_table
        u  = db_context.user_table

        stmt = (select(
            ih.c.id.label("invoice_id"),
            ih.c.sale_date,
            u.c.username,
            p.c.name.label("product_name"),
            il.c.quantity,
            il.c.subtotal.label("subtotal"),
            ih.c.total_amount.label("invoice_total"),).select_from(            
                ih.join(il, ih.c.id == il.c.invoice_id)
                .join(p, il.c.product_id == p.c.id)
                .join(u, ih.c.user_id == u.c.id)).where(ih.c.user_id == user_id).order_by(il.c.id)
                .order_by(ih.c.id)
                .offset((page - 1) * size).limit(size)
                )
        
        with self.engine.connect() as conn:
            invoices = conn.execute(stmt).mappings().all()

            if(len(invoices)==0):
                return None
            else:
                return [dict(i) for i in invoices]
            