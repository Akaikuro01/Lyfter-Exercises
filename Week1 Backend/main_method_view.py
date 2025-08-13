from flask import Flask, request, jsonify
from flask.views import MethodView
import json
import data_handling
import secrets
from functools import wraps

app = Flask(__name__)

def get_task_list_file():
    open_json = data_handling.HandleJson("tasks.json")
    tasks_list = open_json.read_json()
    return tasks_list

def save_task_list_file(tasks_list):
    save_json = data_handling.HandleJson("tasks.json")
    save_json.write_json(tasks_list)

def check_existing_id(tasks_list, id_):
    for task in tasks_list:
        if task["id"] == id_:
            return True
    return False


def check_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token missing"}), 401

        auth_token = auth_header.split(" ")[1]
        if auth_token != token:
            return jsonify({"error": "Invalid token"}), 401
        
        return func(*args, **kwargs)
    return wrapper

token = ""

@app.route("/login")
def validate_credentials():
    global token
    if not request.is_json:
            return jsonify({"message": "Content-Type must be application/json"}), 415
    data = request.get_json()
    #Since this is just an exercise for simulating login logic, I am just hardcoding a username and a password.
    if data.get("username") == "stevenquiros" and data.get("password") == "Patitos123":
        token = secrets.token_hex(16)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
    


class TasksAPI(MethodView):
    decorators = [check_token]

    def get(self):
        try:
            tasks_list = get_task_list_file()
            filtered_tasks = tasks_list
            task_filter = request.args.get("status")
            if task_filter:
                filtered_tasks = list(
                    filter(lambda show: show["status"] == task_filter, filtered_tasks)
                )
            return jsonify(filtered_tasks), 200
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except FileNotFoundError as ex:
            return jsonify(message=str(ex)), 404
        except PermissionError as ex:
            return jsonify(message=str(ex)), 403
        except json.JSONDecodeError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify({"message": f"Unexpected error: {ex}"}), 500


    def post(self):
        try:
            if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}
            tasks_list = get_task_list_file()

            if "status" not in body:
                raise ValueError("error: Status required.")
            if "title" not in body:
                raise ValueError("error: title required.")
            if "id" not in body:
                raise ValueError("error: id required.")
            if "description" not in body:
                raise ValueError("error: description required.")

            if check_existing_id(tasks_list, int(body["id"])):
                return jsonify({"message": "Task id already exists."}), 409

            if body["status"] not in ["Completed", "In progress", "Pending"]:
                return jsonify({"error": "error: Invalid status entered."}), 422

            tasks_list.append(
                {
                    "id": int(body["id"]),
                    "title": body["title"],
                    "description": body["description"],
                    "status": body["status"]
                }
            )

            save_task_list_file(tasks_list)
            return jsonify(tasks_list), 201
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except FileNotFoundError as ex:
            return jsonify(message=str(ex)), 404
        except PermissionError as ex:
            return jsonify(message=str(ex)), 403
        except json.JSONDecodeError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify({"message": f"Unexpected error: {ex}"}), 500

    def put(self, task_id):
        try:
            if not request.is_json:
                return jsonify({"message": "Content-Type must be application/json"}), 415
            body = request.get_json(silent=True) or {}

            tasks_list = get_task_list_file()

            idx_to_modify = -1
            for index, task in enumerate(tasks_list):
                if task["id"] == task_id:
                    idx_to_modify = index
                    break
            
            if idx_to_modify == -1:
                return jsonify({"error": "Task not found"}), 404
            else:
                if "status" not in body:
                    return jsonify({"error": "Status required."}), 400
                if body["status"] not in ["Completed", "In progress", "Pending"]:
                    return jsonify({"error": "error: Invalid status entered."}), 422
                if "title" not in body:
                    return jsonify({"error": "Title required."}), 400
                if "description" not in body:
                    return jsonify({"error": "Description required."}), 400
                
                tasks_list[idx_to_modify] = {
                    "id": task_id,
                    "title": body["title"],
                    "description": body["description"],
                    "status": body["status"]
            }
            save_task_list_file(tasks_list)
            return jsonify(tasks_list), 200
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except FileNotFoundError as ex:
            return jsonify(message=str(ex)), 404
        except PermissionError as ex:
            return jsonify(message=str(ex)), 403
        except json.JSONDecodeError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify({"message": f"Unexpected error: {ex}"}), 500


    def delete(self, task_id):
        try:
            tasks_list = get_task_list_file()
            
            idx_to_modify = -1
            for index, task in enumerate(tasks_list):
                if task["id"] == task_id:
                    idx_to_modify = index
                    break
            
            if idx_to_modify == -1:
                return jsonify({"error": "Task not found"}), 404
            
            tasks_list.pop(idx_to_modify)

            save_task_list_file(tasks_list)
            return jsonify(tasks_list), 204
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except FileNotFoundError as ex:
            return jsonify(message=str(ex)), 404
        except PermissionError as ex:
            return jsonify(message=str(ex)), 403
        except json.JSONDecodeError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify({"message": f"Unexpected error: {ex}"}), 500


task_view = TasksAPI.as_view("task_api")

app.add_url_rule("/tasks", view_func=task_view, methods=["GET", "POST"])
app.add_url_rule("/tasks/<int:task_id>", view_func=task_view, methods=["PUT", "DELETE"])


if __name__ == "__main__":
    app.run(host="localhost", debug=True)