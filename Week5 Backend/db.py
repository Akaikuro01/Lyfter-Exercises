import psycopg2

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")
    
    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname = db_name,
                user = user,
                password = password,
                host = host,
                port = port
            )
            return connection
        except Exception as error:
            raise Exception("Error connecting to the database: ", error)
    
    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Connection closed.")
        except Exception as error:
            raise Exception("Error connecting to the database: ", error)

    def build_where_filters(self, query, filters):
        try:
            where_clause = "WHERE "
            for index, item in enumerate(filters):
                for key, value in item.items():
                    where_clause += f"{key} = '{value}'"
                    if index == len(filters) - 1:
                        where_clause += ";"
                    else:
                        where_clause += " AND "
            query += where_clause
            return query
        except ValueError as error:
            raise ValueError(error)

    def execute_query(self, query, *args):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()

            # Check if the query returend something, if so, return the results
            if self.cursor.description:
                results = self.cursor.fetchall()
                return results
        except Exception as error:
            raise Exception("Error executing query: ", error)