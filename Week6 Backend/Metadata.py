from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

DB_URI = 'postgresql://postgres:Contoso!0000@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30), nullable=False),
    Column("email", String(80), nullable=False),
)

addresses_table = Table(
    "addresses",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("address", String(255), nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
)

vehicle_table = Table(
    "vehicles",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("brand", String(20), nullable=False),
    Column("model", String(50), nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=True),
)

metadata_obj.create_all(engine, checkfirst=True)
print("Tablas verificadas/creadas.")
