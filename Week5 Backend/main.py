from flask import Flask, request, jsonify
import db
import Repositories

app = Flask(__name__)

def open_connection():
    db_manager = db.PgManager(
        host="localhost",
        port=5432,
        user="postgres",
        password="Contoso!0000",
        db_name="rentacar",
    )
    return db_manager


@app.route("/users")
def list_users():
    filters = []
    db_manager = open_connection()
    user_repo = Repositories.UsersRepository(db_manager)
    try:
        if request.args.get("id"):
            filters.append({
                "id": request.args.get("id")
            })
        if request.args.get("name"):
            filters.append({
                "name": request.args.get("name")
            })
        if request.args.get("username"):
            filters.append({
                "username": request.args.get("username")
            })
        if request.args.get("email"):
            filters.append({
                "email": request.args.get("email")
            })
        if request.args.get("date_birth"):
            filters.append({
                "date_birth": request.args.get("date_birth")
            })
        if request.args.get("account_status"):
            filters.append({
                "account_status": request.args.get("account_status")
            })
        
        if (filters == []):
            results = user_repo.get_users_filtered()
        else:
            results = user_repo.get_users_filtered(filters)
        
        db_manager.close_connection()
        return jsonify(results), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/users", methods=["POST"])
def create_user():
    try:
        if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
        body = request.get_json(silent=True) or {}

        db_manager = open_connection()
        user_repo = Repositories.UsersRepository(db_manager)

        if "name" not in body:
            raise ValueError("error: name required.")
        if "username" not in body:
            raise ValueError("error: user name required.")
        if "email" not in body:
            raise ValueError("error: email required.")
        if "password" not in body:
            raise ValueError("error: password required.")
        if "date_birth" not in body:
            raise ValueError("error: date of birth required.")
        
        user_repo.insert_new_user(body["name"], body["username"], body["email"], body["password"], body["date_birth"], "Active")
        db_manager.close_connection()
        return jsonify({"message": "User inserted successfully!"}), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/users/<int:user_id>", methods=["PATCH"])
def modify_user_status(user_id):
    try:
        if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415

        if not request.args.get("status"):
            raise ValueError("error: Need status parameter.")

        status = request.args.get("status")
        db_manager = open_connection()
        user_repo = Repositories.UsersRepository(db_manager)
        
        user_repo.modify_user_status(status, user_id)
        db_manager.close_connection()
        return jsonify({"message": "User's status modified successfully!"}), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/vehicles")
def list_vehicles():
    try:
        filters = []
        db_manager = open_connection()
        car_repo = Repositories.VehicleRepository(db_manager)

        if request.args.get("id"):
            filters.append({
                "id": request.args.get("id")
            })
        if request.args.get("brand"):
            filters.append({
                "brand": request.args.get("brand")
            })
        if request.args.get("model"):
            filters.append({
                "model": request.args.get("model")
            })
        if request.args.get("fabrication_year"):
            filters.append({
                "fabrication_year": request.args.get("fabrication_year")
            })
        if request.args.get("vehicle_status"):
            filters.append({
                "vehicle_status": request.args.get("vehicle_status")
            })

        if (filters == []):
            results = car_repo.get_vehicles_filtered()
        else:
            results = car_repo.get_vehicles_filtered(filters)

        db_manager.close_connection()
        return jsonify(results), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/vehicles", methods=["POST"])
def create_vehicle():
    try:
        if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
        body = request.get_json(silent=True) or {}

        db_manager = open_connection()
        vechilce_repo = Repositories.VehicleRepository(db_manager)

        if "brand" not in body:
            raise ValueError("error: brand required.")
        if "model" not in body:
            raise ValueError("error: model required.")
        if "fabrication_year" not in body:
            raise ValueError("error: fabrication year required.")
        if "vehicle_status" not in body:
            raise ValueError("error: vehicle status required.")
        
        vechilce_repo.insert_new_vehicle(body["brand"], body["model"], body["fabrication_year"], body["vehicle_status"])
        db_manager.close_connection()
        return jsonify({"message": "Vehicle inserted successfully!"}), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/vehicles/<int:vehicle_id>", methods=["PATCH"])
def modify_vehicle_Status(vehicle_id):
    try:
        if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415

        if not request.args.get("status"):
            raise ValueError("error: Need status parameter.")

        status = request.args.get("status")
        db_manager = open_connection()
        vehicle_repo = Repositories.VehicleRepository(db_manager)
        
        vehicle_repo.modify_vehicle_status(status, vehicle_id)
        db_manager.close_connection()
        return jsonify({"message": "Vehicle's status modified successfully!"}), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/rents")
def list_rents():
    try:
        filters = []
        db_manager = open_connection()
        rents_repo = Repositories.UserRentsRepository(db_manager)

        if request.args.get("id"):
            filters.append({
                "id": request.args.get("id")
            })
        if request.args.get("user_id"):
            filters.append({
                "user_id": request.args.get("user_id")
            })
        if request.args.get("vehicle_id"):
            filters.append({
                "vehicle_id": request.args.get("vehicle_id")
            })
        if request.args.get("date_rented"):
            filters.append({
                "date_rented": request.args.get("date_rented")
            })
        if request.args.get("rent_status"):
            filters.append({
                "rent_status": request.args.get("rent_status")
            })

        if (filters == []):
            results = rents_repo.get_rents_filtered()
        else:
            results = rents_repo.get_rents_filtered(filters)

        db_manager.close_connection()
        return jsonify(results), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/rents", methods=["POST"])
def rent_a_car():
    try:
        if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
        body = request.get_json(silent=True) or {}

        db_manager = open_connection()
        rents_repo = Repositories.UserRentsRepository(db_manager)
        vehicle_repo = Repositories.VehicleRepository(db_manager)

        if "user_id" not in body:
            raise ValueError("error: user_id required.")
        if "vehicle_id" not in body:
            raise ValueError("error: vehicle_id required.")
        if "rent_status" not in body:
            raise ValueError("error: rent_status year required.")
        
        rents_repo.rent_a_car(body["user_id"], body["vehicle_id"], body["rent_status"])
        vehicle_repo.modify_vehicle_status("Rented", body["vehicle_id"])
        db_manager.close_connection()
        return jsonify({"message": "Rent inserted successfully!"}), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500


@app.route("/rents/<int:rent_id>", methods=["PATCH"])
def modify_rent_status(rent_id):
    try:
        if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
        body = request.get_json(silent=True) or {}

        if not request.args.get("status"):
            raise ValueError("error: Need status parameter.")

        status = request.args.get("status")
        db_manager = open_connection()
        rent_repo = Repositories.UserRentsRepository(db_manager)
        
        rent_repo.modify_rent_status(status, rent_id)
        db_manager.close_connection()
        return jsonify({"message": "Rent status modified successfully!"}), 200
    except ValueError as error:
        return jsonify(message=str(error)), 400
    except Exception as error:
        return jsonify({"message": f"Unexpected error: {error}"}), 500



if __name__ == "__main__":
    app.run(host="localhost", debug=True)