import db

class UsersRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_user(self, user):
        return {
        "id": user[0],
        "name": user[1],
        "username": user[2],
        "email": user[3],
        "password": user[4],
        "date_birth": user[5].isoformat(),
        "account_status": user[6]
        }
    
    def insert_new_user(self, name, username, email, password, date_birth, account_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (name, username, email, password, date_birth, account_status) VALUES (%s, %s, %s, %s, %s, %s);",
                name, username, email, password, date_birth, account_status
            )
            print("User inserted succesfully!")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False
    
    def modify_user_status(self, status, _id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s;",
                status, _id
            )
            print("User status correctly modified!")
            return True
        except Exception as error:
            print("Error modifying user status: ", error)
            return False


    def get_users_filtered(self, filters = None):
        try:
            # If filters are not provided then just show all data without filters
            if not filters:
                results = self.db_manager.execute_query(
                    "SELECT id, name, username, email, password, date_birth, account_status FROM lyfter_car_rental.users;"
                )
            else:
                initial_query = "SELECT id, name, username, email, password, date_birth, account_status FROM lyfter_car_rental.users "
                query = self.db_manager.build_where_filters(initial_query, filters)
                results = self.db_manager.execute_query(query)
            
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error retrieving all users: ", error)
            return None



class VehicleRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_vehicle(self, vehicle):
        return {
            "id": vehicle[0],
            "brand": vehicle[1],
            "model": vehicle[2],
            "fabrication_year": vehicle[3],
            "vehicle_status": vehicle[4]
        }

    def insert_new_vehicle(self, brand, model, fabrication_year, vehicle_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.vehicles (brand, model, fabrication_year, vehicle_status) VALUES (%s, %s, %s, %s)",
                brand, model, fabrication_year, vehicle_status
            )
            print("Vehicle inserted succesfully!")
            return True
        except Exception as error:
            print("Error inserting a vehicle into the database: ", error)
            return False
    
    def modify_vehicle_status(self, status, _id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.vehicles SET vehicle_status = %s WHERE id = %s",
                status, _id
            )
            print("Vehicle status correctly modified!")
            return True
        except Exception as error:
            print("Error modifying vehicle status: ", error)
            return False
    
    def get_vehicles_filtered(self, filters=None):
        try:
            # If filters are not provided then just show all data without filters
            if not filters:
                results = self.db_manager.execute_query(
                    "SELECT id, brand, model, fabrication_year, vehicle_status FROM lyfter_car_rental.vehicles;"
                )
            else:
                initial_query = "SELECT id, brand, model, fabrication_year, vehicle_status FROM lyfter_car_rental.vehicles "
                query = self.db_manager.build_where_filters(initial_query, filters)
                results = self.db_manager.execute_query(query)

            formatted_results = [self._format_vehicle(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error retrieving all users: ", error)
            return None



class UserRentsRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_rents(self, rent):
        return {
            "id": rent[0],
            "user_id": rent[1],
            "vehicle_id": rent[2],
            "date_rented": rent[3],
            "rent_status": rent[4]
        }

    def rent_a_car(self, user_id, vehicle_id, rent_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.user_rents (user_id, vehicle_id, rent_status) VALUES (%s, %s, %s);",
                user_id, vehicle_id, rent_status
            )
            print("Rent inserted succesfully!")
            return True
        except Exception as error:
            print("Error inserting a rent into the database: ", error)
            return False
    
    def modify_rent_status(self, status, _id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.user_rents SET rent_status = %s WHERE id = %s;",
                status, _id
            )
            print("Rent status correctly modified!")
            return True
        except Exception as error:
            print("Error modifying rent status: ", error)
            return False

    def get_rents_filtered(self, filters=None):
        try:
            # If filters are not provided then just show all data without filters
            if not filters:
                results = self.db_manager.execute_query(
                    "SELECT id, user_id, vehicle_id, date_rented, rent_status FROM lyfter_car_rental.user_rents;"
                )
            else:
                initial_query = "SELECT id, user_id, vehicle_id, date_rented, rent_status FROM lyfter_car_rental.user_rents "
                query = self.db_manager.build_where_filters(initial_query, filters)
                results = self.db_manager.execute_query(query)
            formatted_results = [self._format_rents(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error retrieving all users: ", error)
            return None