from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Float, Date, ForeignKey, Boolean, DateTime

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
            Column("full_name", String(30), nullable=False),
            Column("email", String(30), nullable=False),
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
            Column("invoice_address", String(120), nullable=False),
            Column("payment_method", Integer, ForeignKey("payment_methods.id"), nullable=False),
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
        self.shopping_cart_table = Table(
            "shopping_cart",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("user_id", ForeignKey("users.id")),
            Column("date_created", Date, nullable=False)
        )
        self.cart_items_table = Table(
            "cart_items",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("cart_id", ForeignKey("shopping_cart.id", ondelete="CASCADE")),
            Column("product_id", ForeignKey("products.id"), nullable=False),
            Column("quantity", Integer, nullable=False)
        )
        self.payment_methods_table = Table(
            "payment_methods", self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("user_id", ForeignKey("users.id"), nullable=False),
            Column("brand", String(20)),                    
            Column("last4", String(4)),
            Column("exp_month", Integer),
            Column("exp_year", Integer)
        )
        self.engine = create_engine('postgresql://postgres:Contoso!0000@localhost:5432/petshop')
        self.metadata_obj.create_all(self.engine)


db_context = DBContext()
