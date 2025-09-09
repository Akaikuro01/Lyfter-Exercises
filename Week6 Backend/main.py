import Metadata
import Repositories



if __name__ == "__main__":
    users = Metadata.user_table
    addresses = Metadata.addresses_table
    vehicles = Metadata.vehicle_table
    engine = Metadata.engine

    user_repo = Repositories.UsersRepository(engine, users)
    address_repo = Repositories.AddressRepository(engine, addresses)
    vehicles_repo = Repositories.VehicleRepository(engine, vehicles)

    # Insert values
    user_repo.insert_user("Steven", "stv@hotmail.com")
    address_repo.insert_address("Somewhere in Cartago", 1)
    vehicles_repo.insert_vehicle("Honda", "Civic", 1)

    user_repo.insert_user("Altair", "alt@hotmail.com")
    address_repo.insert_address("Somewhere in Jerusalem", 2)
    vehicles_repo.insert_vehicle("Toyota", "Corolla")    

    user_repo.insert_user("Kuma", "kum@hotmail.com")
    address_repo.insert_address("Somewhere in Jerusalem", 3)
    vehicles_repo.insert_vehicle("Mitsubishi", "Lancer", 3)   

    # Get all values from each table
    print("======================After Inserts===========================")
    all_users = user_repo.get_all_users()
    print(all_users)
    print("==============================================================")
    all_addresses = address_repo.get_all_addresses()
    print(all_addresses)
    print("==============================================================")
    all_vehicles = vehicles_repo.get_all_vehicles()
    print(all_vehicles)
    print("==============================================================")

    # Update each
    user_repo.update_user_by_id(1, "Steven", "stv44@hotmail.com")
    address_repo.update_address_by_id(2, "Somewhere in Masyaf", 2)
    # Here I assign a vehicle to Altair *fulfilling requirement 4.d* 
    vehicles_repo.update_vehicle_by_id(2, "Toyota", "Corolla", 2)


    # Get all values from each table after updates
    print("===================After Updates==============================")
    all_users = user_repo.get_all_users()
    print(all_users)
    print("==============================================================")
    all_addresses = address_repo.get_all_addresses()
    print(all_addresses)
    print("==============================================================")
    all_vehicles = vehicles_repo.get_all_vehicles()
    print(all_vehicles)
    print("==============================================================")

    # Deletes 
    vehicles_repo.delete_vehicle_by_id(2)
    address_repo.delete_address_by_id(2)
    user_repo.delete_user_by_id(2)

        # Get all values from each table after delets
    print("=================After Deletes================================")
    all_users = user_repo.get_all_users()
    print(all_users)
    print("==============================================================")
    all_addresses = address_repo.get_all_addresses()
    print(all_addresses)
    print("==============================================================")
    all_vehicles = vehicles_repo.get_all_vehicles()
    print(all_vehicles)
    print("==============================================================")