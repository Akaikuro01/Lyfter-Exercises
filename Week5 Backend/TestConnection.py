import psycopg2
from datetime import date

def format_user(user):
    return {
        "id": user[0],
        "name": user[1],
        "username": user[2],
        "email": user[3],
        "password": user[4],
        "birth_date": user[5].isoformat(),
        "account_status": user[6]
    }

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="Contoso!0000",
    dbname="rentacar",
)

print("Connected to the database")

cursor = connection.cursor()

cursor.execute("SELECT * FROM lyfter_car_rental.users WHERE id = 1")
print("Query executed")

results = cursor.fetchall()
formatted_results = [format_user(result) for result in results]
print(formatted_results)


def build_where_filters(query, filters):
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

query = "SELECT id, name, username, email, password, date_birth, account_status FROM lyfter_car_rental.users "
filters = [{"id": 1}, {"name": "Ryan Johnson"}]



print(build_where_filters(query, filters))


# Things to ask: 
# Exception handling in repositories and db modules
# _id naming in the repositories
# Where build, is it ok? Is it safe?
# renting a car, it is also updating the status of the car in the same function
# main code organization, is that ok? should I divide? How?
# Changing the status of a rent, in the requirements it says it should let you set a user overdue. That's already possible with the modify_rent_status function.
# Check overal I am not missing anything
# Connection handling, is it ok the way I am opening and closing?