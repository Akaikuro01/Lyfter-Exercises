from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Float, Date, ForeignKey

class DBContext:
    def __init__(self):        
        self.metadata_obj = MetaData()
        
        self.roles_table = Table(
        "roles",
        self.metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(5), unique=True, nullable=False)
        )
        self.user_table = Table(
            "users",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("username", String(30), nullable=False),
            Column("password", String, nullable=False),
            Column("role_id", Integer, ForeignKey("roles.id"), nullable=False)
        )
        self.product_table = Table(
            "products",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("name", String(30), nullable=False),
            Column("unit_price", Float, nullable=False),
            Column("entry_date", Date, nullable=False),
            Column("stock_qty", Integer, nullable=False)
        )
        self.invoice_header_table = Table(
            "invoice_headers",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("sale_date", Date, nullable=False),
            Column("total_amount", Float, nullable=False),
            Column("user_id", ForeignKey("users.id"))
        )
        self.invoice_lines_table = Table(
            "invoice_lines",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("quantity", Integer, nullable=False),
            Column("unit_price", Float, nullable=False),
            Column("subtotal", Float, nullable=False),
            Column("product_id", ForeignKey("products.id"), nullable=False),
            Column("invoice_id", ForeignKey("invoice_headers.id"), nullable=False)
        )
        self.engine = create_engine('postgresql://postgres:Contoso!0000@localhost:5432/sales')
        self.metadata_obj.create_all(self.engine)


db_context = DBContext()
